from __future__ import annotations

from typing import Any

from src.mgc.transport import Transport


class Backups:
    """Manage compute backup operations."""

    def __init__(self, transport: Transport):
        """Create a backup resource client.

        Args:
            transport: Shared transport used to send API requests.
        """
        self._transport = transport

    async def list(
        self,
        *,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """List backups.

        Args:
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing backup data.
        """

        params = {}

        if expand:
            params["expand"] = expand

        return await self._transport.get(
            "compute/v1/backups",
            params=params,
        )

    async def get(
        self,
        backup_id: str,
        *,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """Get a backup by ID.

        Args:
            backup_id: ID of the backup to retrieve.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing backup data.
        """

        params = {}

        if expand:
            params["expand"] = expand

        return await self._transport.get(
            f"compute/v1/backups/{backup_id}",
            params=params,
        )

    async def create(
        self,
        *,
        instance_id: str,
        name: str,
    ) -> dict[str, Any]:
        """Create a backup from a virtual machine.

        Args:
            instance_id: ID of the source virtual machine.
            name: Name for the new backup.

        Returns:
            Parsed API response containing the created backup data.
        """

        payload = {
            "instance": {
                "id": instance_id,
            },
            "name": name,
        }

        return await self._transport.post(
            "compute/v1/backups",
            json=payload,
        )

    async def delete(
        self,
        backup_id: str,
    ) -> None:
        """Delete a backup.

        Args:
            backup_id: ID of the backup to delete.
        """

        await self._transport.delete(
            f"compute/v1/backups/{backup_id}",
        )

    async def rename(
        self,
        backup_id: str,
        name: str,
    ) -> None:
        """Rename a backup.

        Args:
            backup_id: ID of the backup to rename.
            name: New name for the backup.
        """

        await self._transport.patch(
            f"compute/v1/backups/{backup_id}/rename",
            json={
                "name": name,
            },
        )

    async def copy(
        self,
        backup_id: str,
        *,
        region: str,
    ) -> None:
        """Copy a backup to another region.

        Args:
            backup_id: ID of the backup to copy.
            region: Target region for the copied backup.
        """

        await self._transport.post(
            f"compute/v1/backups/{backup_id}/copy",
            json={
                "region": region,
            },
        )

    async def restore(
        self,
        backup_id: str,
        *,
        name: str,
        machine_type_id: str,
        ssh_key_name: str,
        availability_zone: str | None = None,
        network: dict | None = None,
        user_data: str | None = None,
    ) -> dict[str, Any]:
        """Restore a backup into a virtual machine.

        Args:
            backup_id: ID of the backup to restore.
            name: Name for the restored virtual machine.
            machine_type_id: ID of the machine type to assign.
            ssh_key_name: SSH key name to configure on the virtual machine.
            availability_zone: Optional availability zone for the virtual machine.
            network: Optional network configuration.
            user_data: Optional user data script or cloud-init content.

        Returns:
            Parsed API response containing the restored virtual machine data.
        """

        payload = {
            "name": name,
            "machine_type": {
                "id": machine_type_id,
            },
            "ssh_key_name": ssh_key_name,
            "network": network or {},
        }

        if availability_zone:
            payload["availability_zone"] = availability_zone

        if user_data:
            payload["user_data"] = user_data

        return await self._transport.post(
            f"compute/v1/backups/{backup_id}/restore",
            json=payload,
        )
