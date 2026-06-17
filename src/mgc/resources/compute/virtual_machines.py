from __future__ import annotations

from typing import Any

from src.mgc.transport import Transport


class VirtualMachines:
    """Manage compute virtual machine operations."""

    def __init__(self, transport: Transport):
        """Create a virtual machine resource client.

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
        """List virtual machines.

        Args:
            limit: Maximum number of virtual machines to return.
            offset: Number of virtual machines to skip before returning results.
            sort: Optional API sort expression.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing virtual machine data.
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
            "compute/v1/instances",
            params=params,
        )

    async def get(
        self,
        instance_id: str,
        *,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:
        """Get a virtual machine by ID.

        Args:
            instance_id: ID of the virtual machine to retrieve.
            expand: Optional related fields to expand in the response.

        Returns:
            Parsed API response containing virtual machine data.
        """

        params = {}

        if expand:
            params["expand"] = expand

        return await self._transport.get(
            f"compute/v1/instances/{instance_id}",
            params=params,
        )

    async def create(
        self,
        *,
        name: str,
        image_id: str,
        machine_type_id: str,
        ssh_key_name: str,
        availability_zone: str | None = None,
        user_data: str | None = None,
        network: dict | None = None,
    ) -> dict[str, Any]:
        """Create a virtual machine.

        Args:
            name: Name for the new virtual machine.
            image_id: ID of the image used to create the virtual machine.
            machine_type_id: ID of the machine type to assign.
            ssh_key_name: SSH key name to configure on the virtual machine.
            availability_zone: Optional availability zone for the virtual machine.
            user_data: Optional user data script or cloud-init content.
            network: Optional network configuration.

        Returns:
            Parsed API response containing the created virtual machine data.
        """
        payload = {
            "name": name,
            "image": {
                "id": image_id,
            },
            "machine_type": {
                "id": machine_type_id,
            },
            "ssh_key_name": ssh_key_name,
        }

        if availability_zone:
            payload["availability_zone"] = availability_zone

        if user_data:
            payload["user_data"] = user_data

        if network:
            payload["network"] = network

        return await self._transport.post(
            "/v1/instances",
            json=payload,
        )

    async def delete(
        self,
        instance_id: str,
        *,
        delete_public_ip: bool = False,
    ) -> None:
        """Delete a virtual machine.

        Args:
            instance_id: ID of the virtual machine to delete.
            delete_public_ip: Whether to delete the associated public IP.
        """

        await self._transport.delete(
            f"compute/v1/instances/{instance_id}",
            params={
                "delete_public_ip": delete_public_ip,
            },
        )

    async def start(
        self,
        instance_id: str,
    ) -> None:
        """Start a virtual machine.

        Args:
            instance_id: ID of the virtual machine to start.
        """

        await self._transport.post(f"compute/v1/instances/{instance_id}/start")

    async def stop(
        self,
        instance_id: str,
    ) -> None:
        """Stop a virtual machine.

        Args:
            instance_id: ID of the virtual machine to stop.
        """

        await self._transport.post(f"compute/v1/instances/{instance_id}/stop")

    async def reboot(
        self,
        instance_id: str,
    ) -> None:
        """Reboot a virtual machine.

        Args:
            instance_id: ID of the virtual machine to reboot.
        """

        await self._transport.post(f"compute/v1/instances/{instance_id}/reboot")

    async def suspend(
        self,
        instance_id: str,
    ) -> None:
        """Suspend a virtual machine.

        Args:
            instance_id: ID of the virtual machine to suspend.
        """

        await self._transport.post(f"compute/v1/instances/{instance_id}/suspend")

    async def rename(
        self,
        instance_id: str,
        name: str,
    ) -> None:
        """Rename a virtual machine.

        Args:
            instance_id: ID of the virtual machine to rename.
            name: New name for the virtual machine.
        """

        await self._transport.patch(
            f"compute/v1/instances/{instance_id}/rename",
            json={
                "name": name,
            },
        )

    async def retype(
        self,
        instance_id: str,
        machine_type_id: str,
    ) -> None:
        """Change the machine type of a virtual machine.

        Args:
            instance_id: ID of the virtual machine to update.
            machine_type_id: ID of the new machine type.
        """

        await self._transport.post(
            f"compute/v1/instances/{instance_id}/retype",
            json={
                "machine_type": {
                    "id": machine_type_id,
                }
            },
        )
