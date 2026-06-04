# transport.py

from importlib.metadata import PackageNotFoundError, version
from typing import Any

import httpx

from .auth import AuthProvider
from .config import ClientConfig


def get_package_version() -> str:
    try:
        return version("mgc-sdk-python")
    except PackageNotFoundError as error:
        print(error)
        return "0.0.0"
    
class Transport:

    def __init__(
        self,
        *,
        auth: AuthProvider,
        config: ClientConfig,
    ):
        self._auth = auth
        self._config = config

        self._client = httpx.AsyncClient(
            base_url=self._build_base_url(),
            timeout=config.timeout,
            headers=self._build_headers(),
        )

    def _build_base_url(self) -> str:
        return (
            f"https://api.magalu.cloud/"
            f"{self._config.region}"
        )

    def _build_headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "User-Agent": f"mgc-python/{get_package_version()}",
            **self._auth.get_access_token(),
        }

    async def request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> Any:

        response = await self._client.request(
            method=method,
            url=f"{self._client.base_url}{path}",
            **kwargs,
        )
        print(self._client.headers)

        if not response.is_success and response.headers.get(
                "content-type",
                ""
            ).startswith("application/json"):
                raise Exception(response.json())

        if response.status_code == 204:
            return None

        if response.headers.get(
            "content-type",
            ""
        ).startswith("application/json"):
            return response.json()
        
        return response.text
    
    async def get(
        self,
        path: str,
        **kwargs,
    ):
        return await self.request(
            "GET",
            path,
            **kwargs,
        )
    
    async def post(
        self,
        path: str,
        **kwargs,
    ):
        return await self.request(
            "POST",
            path,
            **kwargs,
        )

    async def put(
        self,
        path: str,
        **kwargs,
    ):
        return await self.request(
            "PUT",
            path,
            **kwargs,
        )

    async def patch(
        self,
        path: str,
        **kwargs,
    ):
        return await self.request(
            "PATCH",
            path,
            **kwargs,
        )

    async def delete(
        self,
        path: str,
        **kwargs,
    ):
        return await self.request(
            "DELETE",
            path,
            **kwargs,
        )

    async def close(self):
        await self._client.aclose()