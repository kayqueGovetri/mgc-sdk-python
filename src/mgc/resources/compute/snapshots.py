from __future__ import annotations

from typing import Any

from src.mgc.transport import Transport


class Snapshots:
    """Manage compute snapshot operations."""

    def __init__(self, transport: Transport):
        """Create a snapshot resource client.

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
        """List snapshots.

        Args:
            limit: Maximum number of snapshots to return.
            offset: Number of snapshots to skip before returning results.
            sort: Optional API sort expression.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing snapshot data.
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
            "compute/v1/snapshots",
            params=params,
        )

    async def get(
        self,
        snapshot_id: str,
        *,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """Get a snapshot by ID.

        Args:
            snapshot_id: ID of the snapshot to retrieve.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing snapshot data.
        """

        params = {}

        if expand:
            params["expand"] = expand

        return await self._transport.get(
            f"compute/v1/snapshots/{snapshot_id}",
            params=params,
        )

    async def create(
        self,
        *,
        instance_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        """Create a snapshot from a virtual machine.

        Args:
            instance_id: ID of the source virtual machine.
            name: Optional name for the snapshot.
            description: Optional description for the snapshot.

        Returns:
            Parsed API response containing the created snapshot data.
        """

        payload = {
            "instance_id": instance_id,
        }

        if name:
            payload["name"] = name

        if description:
            payload["description"] = description

        return await self._transport.post(
            "compute/v1/snapshots",
            json=payload,
        )

    async def delete(
        self,
        snapshot_id: str,
    ) -> None:
        """Delete a snapshot.

        Args:
            snapshot_id: ID of the snapshot to delete.
        """

        await self._transport.delete(
            f"compute/v1/snapshots/{snapshot_id}",
        )

    async def restore(
        self,
        snapshot_id: str,
        *,
        instance_id: str | None = None,
    ) -> dict[str, Any]:
        """Restore a snapshot.

        Args:
            snapshot_id: ID of the snapshot to restore.
            instance_id: Optional target virtual machine ID.

        Returns:
            Parsed API response containing restore data.
        """

        payload = {}

        if instance_id:
            payload["instance_id"] = instance_id

        return await self._transport.post(
            f"compute/v1/snapshots/{snapshot_id}/restore",
            json=payload,
        )

    async def create_from_instance(
        self,
        *,
        instance_id: str,
        name: str | None = None,
    ) -> dict[str, Any]:
        """Create a snapshot from a virtual machine instance.

        Args:
            instance_id: ID of the source virtual machine.
            name: Optional name for the snapshot.

        Returns:
            Parsed API response containing the created snapshot data.
        """

        payload = {
            "instance_id": instance_id,
        }

        if name:
            payload["name"] = name

        return await self._transport.post(
            "compute/v1/snapshots",
            json=payload,
        )
