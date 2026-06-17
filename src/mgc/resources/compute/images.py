from __future__ import annotations

from typing import Any

from src.mgc.transport import Transport


class Images:
    """Manage compute image operations."""

    def __init__(self, transport: Transport):
        """Create an image resource client.

        Args:
            transport: Shared transport used to send API requests.
        """
        self._transport = transport

    async def list(
        self,
        *,
        limit: int = 50,
        offset: int = 0,
        sort: str | None = None,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """List available compute images.

        Args:
            limit: Maximum number of images to return.
            offset: Number of images to skip before returning results.
            sort: Optional API sort expression.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing image data.
        """

        params = {
            "_limit": limit,
            "_offset": offset,
        }

        if sort:
            params["_sort"] = sort

        if expand:
            params["expand"] = expand

        return await self._transport.get(
            "compute/v1/images",
            params=params,
        )
