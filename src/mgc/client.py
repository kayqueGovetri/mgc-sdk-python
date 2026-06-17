from src.mgc.config import ClientConfig

from .auth import AuthProvider
from .resources.compute.compute import Compute
from .transport import Transport


class ApiKeyAuth(AuthProvider):
    """Authenticate SDK requests with a Magalu Cloud API key."""

    def __init__(self, api_key: str):
        """Initialize API key authentication.

        Args:
            api_key: Magalu Cloud API key used in request headers.
        """
        self._api_key = api_key

    def get_access_token(self) -> str:
        """Return the API key authentication header."""
        auth_headers = {
            "X-API-Key": self._api_key,
        }
        return auth_headers


class Client:
    """Asynchronous root client for the Magalu Cloud SDK."""

    def __init__(self, *, api_key: str, config=None):
        """Create a client with authenticated access to SDK resources.

        Args:
            api_key: Magalu Cloud API key used to authenticate requests.
            config: Optional client configuration. Defaults to `ClientConfig()`.
        """
        self._config = config or ClientConfig()

        self._transport = Transport(
            auth=ApiKeyAuth(api_key),
            config=self._config,
        )

        self.compute = Compute(self._transport)

    async def close(self) -> None:
        """Close the underlying HTTP transport."""
        await self._transport.close()

    async def __aenter__(self):
        """Enter the asynchronous context manager and return this client."""
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Close the client when leaving an asynchronous context manager."""
        await self.close()
