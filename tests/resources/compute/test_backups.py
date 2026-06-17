import asyncio

import pytest

from src.mgc.resources.compute.backups import Backups


def run(coro):
    return asyncio.run(coro)


def make_resource(fake_transport):
    return Backups(fake_transport)


@pytest.mark.parametrize(
    ("expand", "expected_params"),
    [
        (None, {}),
        (["instance"], {"expand": ["instance"]}),
    ],
)
def test_list_builds_params(fake_transport, expand, expected_params):
    resource = make_resource(fake_transport)

    result = run(resource.list(expand=expand))
    assert result == {
        "method": "get",
        "path": "compute/v1/backups",
        "kwargs": {"params": expected_params},
    }
    assert fake_transport.calls == [result]


@pytest.mark.parametrize(
    ("expand", "expected_params"),
    [
        (None, {}),
        (["instance"], {"expand": ["instance"]}),
    ],
)
def test_get_builds_params(fake_transport, expand, expected_params):
    resource = make_resource(fake_transport)

    result = run(resource.get("backup-1", expand=expand))
    assert result == {
        "method": "get",
        "path": "compute/v1/backups/backup-1",
        "kwargs": {"params": expected_params},
    }
    assert fake_transport.calls == [result]


def test_create_posts_instance_and_name_payload(fake_transport):
    resource = make_resource(fake_transport)

    run(resource.create(instance_id="vm-1", name="backup-1"))

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "compute/v1/backups",
            "kwargs": {"json": {"instance": {"id": "vm-1"}, "name": "backup-1"}},
        }
    ]


def test_delete_deletes_backup(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.delete("backup-1")) is None
    assert fake_transport.calls == [{"method": "delete", "path": "compute/v1/backups/backup-1", "kwargs": {}}]


def test_rename_patches_rename_endpoint(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.rename("backup-1", "new-name")) is None
    assert fake_transport.calls == [
        {
            "method": "patch",
            "path": "compute/v1/backups/backup-1/rename",
            "kwargs": {"json": {"name": "new-name"}},
        }
    ]


def test_copy_posts_region_payload(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.copy("backup-1", region="br-ne1")) is None
    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "compute/v1/backups/backup-1/copy",
            "kwargs": {"json": {"region": "br-ne1"}},
        }
    ]


def test_restore_posts_minimal_payload_with_default_network(fake_transport):
    resource = make_resource(fake_transport)

    run(
        resource.restore(
            "backup-1",
            name="vm-restored",
            machine_type_id="type-1",
            ssh_key_name="key-1",
        )
    )

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "compute/v1/backups/backup-1/restore",
            "kwargs": {
                "json": {
                    "name": "vm-restored",
                    "machine_type": {"id": "type-1"},
                    "ssh_key_name": "key-1",
                    "network": {},
                }
            },
        }
    ]


def test_restore_includes_optional_payload_fields(fake_transport):
    resource = make_resource(fake_transport)

    run(
        resource.restore(
            "backup-1",
            name="vm-restored",
            machine_type_id="type-1",
            ssh_key_name="key-1",
            availability_zone="br-se1-a",
            network={"id": "net-1"},
            user_data="#!/bin/sh",
        )
    )

    assert fake_transport.calls[0] == {
        "method": "post",
        "path": "compute/v1/backups/backup-1/restore",
        "kwargs": {
            "json": {
                "name": "vm-restored",
                "machine_type": {"id": "type-1"},
                "ssh_key_name": "key-1",
                "network": {"id": "net-1"},
                "availability_zone": "br-se1-a",
                "user_data": "#!/bin/sh",
            }
        },
    }
