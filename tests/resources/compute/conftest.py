import pytest


class FakeTransport:
    def __init__(self):
        self.calls = []

    async def get(self, path, **kwargs):
        self.calls.append({"method": "get", "path": path, "kwargs": kwargs})
        return {"method": "get", "path": path, "kwargs": kwargs}

    async def post(self, path, **kwargs):
        self.calls.append({"method": "post", "path": path, "kwargs": kwargs})
        return {"method": "post", "path": path, "kwargs": kwargs}

    async def patch(self, path, **kwargs):
        self.calls.append({"method": "patch", "path": path, "kwargs": kwargs})

    async def delete(self, path, **kwargs):
        self.calls.append({"method": "delete", "path": path, "kwargs": kwargs})


@pytest.fixture
def fake_transport():
    return FakeTransport()
