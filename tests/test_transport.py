import asyncio
from importlib.metadata import PackageNotFoundError

import pytest

from src.mgc import transport as transport_module
from src.mgc.config import ClientConfig
from src.mgc.region import Region
from src.mgc.transport import Transport, get_package_version


def run(coro):
    return asyncio.run(coro)


class FakeAuth:
    def get_access_token(self):
        return {"X-API-Key": "secret-key"}


class FakeResponse:
    def __init__(self, *, status_code=200, headers=None, json_data=None, text=""):
        self.status_code = status_code
        self.headers = headers or {}
        self._json_data = json_data
        self.text = text
        self.is_success = 200 <= status_code < 400

    def json(self):
        return self._json_data


class FakeAsyncClient:
    instances = []

    def __init__(self, *, base_url, timeout, headers):
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers
        self.responses = []
        self.calls = []
        self.closed = False
        self.__class__.instances.append(self)

    async def request(self, *, method, url, **kwargs):
        self.calls.append({"method": method, "url": url, "kwargs": kwargs})
        return self.responses.pop(0)

    async def aclose(self):
        self.closed = True


@pytest.fixture(autouse=True)
def fake_async_client(monkeypatch):
    FakeAsyncClient.instances.clear()
    monkeypatch.setattr(transport_module.httpx, "AsyncClient", FakeAsyncClient)
    monkeypatch.setattr(transport_module, "get_package_version", lambda: "1.2.3")


def make_transport(config=None):
    return Transport(auth=FakeAuth(), config=config or ClientConfig())


def test_get_package_version_returns_installed_package_version(monkeypatch):
    monkeypatch.setattr(transport_module, "version", lambda package_name: f"{package_name}:9.9.9")

    assert get_package_version() == "mgc-sdk-python:9.9.9"


def test_get_package_version_falls_back_when_package_is_not_found(monkeypatch):
    def raise_package_not_found(package_name):
        raise PackageNotFoundError(package_name)

    monkeypatch.setattr(transport_module, "version", raise_package_not_found)

    assert get_package_version() == "0.0.0"


def test_transport_initializes_http_client_with_base_url_timeout_and_headers():
    config = ClientConfig(region=Region.BR_NE1, timeout=12.5)

    make_transport(config)

    client = FakeAsyncClient.instances[0]
    assert client.base_url == "https://api.magalu.cloud/br-ne-1"
    assert client.timeout == 12.5
    assert client.headers == {
        "Accept": "application/json",
        "User-Agent": "mgc-python/1.2.3",
        "X-API-Key": "secret-key",
    }


def test_build_base_url_uses_configured_region():
    transport = make_transport(ClientConfig(region=Region.BR_NE1))

    assert transport._build_base_url() == "https://api.magalu.cloud/br-ne-1"


def test_build_headers_merges_defaults_user_agent_and_auth_headers():
    transport = make_transport()

    assert transport._build_headers() == {
        "Accept": "application/json",
        "User-Agent": "mgc-python/1.2.3",
        "X-API-Key": "secret-key",
    }


def test_request_returns_json_response_and_passes_kwargs():
    transport = make_transport()
    client = FakeAsyncClient.instances[0]
    client.responses.append(FakeResponse(headers={"content-type": "application/json"}, json_data={"id": "vm-1"}))

    result = run(transport.request("GET", "/v1/resources", params={"limit": 1}))

    assert result == {"id": "vm-1"}
    assert client.calls == [
        {
            "method": "GET",
            "url": "https://api.magalu.cloud/br-se1/v1/resources",
            "kwargs": {"params": {"limit": 1}},
        }
    ]


def test_request_returns_none_for_204_response():
    transport = make_transport()
    client = FakeAsyncClient.instances[0]
    client.responses.append(FakeResponse(status_code=204, headers={"content-type": "application/json"}))

    assert run(transport.request("DELETE", "/v1/resources/vm-1")) is None


def test_request_returns_text_for_non_json_response():
    transport = make_transport()
    client = FakeAsyncClient.instances[0]
    client.responses.append(FakeResponse(headers={"content-type": "text/plain"}, text="ok"))

    assert run(transport.request("GET", "/health")) == "ok"


def test_request_raises_payload_for_json_error_response():
    transport = make_transport()
    client = FakeAsyncClient.instances[0]
    client.responses.append(
        FakeResponse(status_code=400, headers={"content-type": "application/json"}, json_data={"message": "invalid"})
    )

    try:
        run(transport.request("POST", "/v1/resources"))
    except Exception as exc:
        assert exc.args == ({"message": "invalid"},)
    else:
        pytest.fail("Expected request to raise for JSON error response")


@pytest.mark.parametrize(
    ("helper", "expected_method"),
    [
        ("get", "GET"),
        ("post", "POST"),
        ("put", "PUT"),
        ("patch", "PATCH"),
        ("delete", "DELETE"),
    ],
)
def test_http_method_helpers_delegate_to_request(monkeypatch, helper, expected_method):
    transport = make_transport()
    calls = []

    async def fake_request(method, path, **kwargs):
        calls.append((method, path, kwargs))
        return {"ok": True}

    monkeypatch.setattr(transport, "request", fake_request)

    result = run(getattr(transport, helper)("/path", json={"name": "test"}))

    assert result == {"ok": True}
    assert calls == [(expected_method, "/path", {"json": {"name": "test"}})]


def test_close_closes_http_client():
    transport = make_transport()
    client = FakeAsyncClient.instances[0]

    run(transport.close())

    assert client.closed is True
