from typing import Any

from src.mgc.transport import Transport


class Backups:
    def __init__(self, transport: Transport):
        self._transport = transport

    async def list(
        self,
        *,
        expand: list[str] | None = None,
    ) -> dict[str, Any]:

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

        await self._transport.delete(
            f"compute/v1/backups/{backup_id}",
        )

    async def rename(
        self,
        backup_id: str,
        name: str,
    ) -> None:

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