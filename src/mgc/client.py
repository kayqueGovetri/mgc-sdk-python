from src.mgc.config import ClientConfig

from .auth import AuthProvider
from .resources.compute.compute import Compute
from .transport import Transport


class ApiKeyAuth(AuthProvider):

    def __init__(self, api_key: str):
        self._api_key = api_key

    def get_access_token(self) -> str:
        auth_headers = {
            "X-API-Key": self._api_key,
        }
        return auth_headers
    

class Client:

    def __init__(self, *, api_key: str, config=None):
        self._config = config or ClientConfig()

        self._transport = Transport(
            auth=ApiKeyAuth(api_key),
            config=self._config,
        )

        self.compute = Compute(self._transport)

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()