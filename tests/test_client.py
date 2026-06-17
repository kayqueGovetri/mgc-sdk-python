import asyncio
import sys
import types

from src.mgc.config import ClientConfig
from src.mgc.region import Region

fake_compute_module = types.ModuleType("src.mgc.resources.compute.compute")


class ImportedCompute:
    def __init__(self, transport):
        self.transport = transport


fake_compute_module.Compute = ImportedCompute
sys.modules["src.mgc.resources.compute.compute"] = fake_compute_module

from src.mgc import client as client_module  # noqa: E402
from src.mgc.client import ApiKeyAuth, Client  # noqa: E402


def run(coro):
    return asyncio.run(coro)


def test_api_key_auth_returns_api_key_header():
    auth = ApiKeyAuth("secret-key")

    headers = auth.get_access_token()

    assert headers == {"X-API-Key": "secret-key"}


def test_client_uses_default_config_and_exposes_compute(monkeypatch):
    created = {}

    class FakeTransport:
        def __init__(self, *, auth, config):
            created["auth"] = auth
            created["config"] = config
            self.closed = False

        async def close(self):
            self.closed = True

    class FakeCompute:
        def __init__(self, transport):
            self.transport = transport

    monkeypatch.setattr(client_module, "Transport", FakeTransport)
    monkeypatch.setattr(client_module, "Compute", FakeCompute)

    client = Client(api_key="secret-key")

    assert isinstance(created["config"], ClientConfig)
    assert created["config"].region == Region.BR_SE1
    assert created["auth"].get_access_token() == {"X-API-Key": "secret-key"}
    assert isinstance(client.compute, FakeCompute)
    assert client.compute.transport is client._transport


def test_client_uses_custom_config(monkeypatch):
    created = {}
    config = ClientConfig(region=Region.BR_NE1, timeout=5.0)

    class FakeTransport:
        def __init__(self, *, auth, config):
            created["config"] = config

    class FakeCompute:
        def __init__(self, transport):
            self.transport = transport

    monkeypatch.setattr(client_module, "Transport", FakeTransport)
    monkeypatch.setattr(client_module, "Compute", FakeCompute)

    Client(api_key="secret-key", config=config)

    assert created["config"] is config


def test_client_close_delegates_to_transport(monkeypatch):
    class FakeTransport:
        def __init__(self, *, auth, config):
            self.closed = False

        async def close(self):
            self.closed = True

    class FakeCompute:
        def __init__(self, transport):
            self.transport = transport

    monkeypatch.setattr(client_module, "Transport", FakeTransport)
    monkeypatch.setattr(client_module, "Compute", FakeCompute)
    client = Client(api_key="secret-key")

    run(client.close())

    assert client._transport.closed is True


def test_client_async_context_manager_closes_transport(monkeypatch):
    class FakeTransport:
        def __init__(self, *, auth, config):
            self.closed = False

        async def close(self):
            self.closed = True

    class FakeCompute:
        def __init__(self, transport):
            self.transport = transport

    monkeypatch.setattr(client_module, "Transport", FakeTransport)
    monkeypatch.setattr(client_module, "Compute", FakeCompute)

    async def use_client():
        async with Client(api_key="secret-key") as client:
            assert isinstance(client, Client)
            return client

    client = run(use_client())

    assert client._transport.closed is True
