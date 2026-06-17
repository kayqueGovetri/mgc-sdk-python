import asyncio

import pytest

from src.mgc.resources.compute.virtual_machines import VirtualMachines


def run(coro):
    return asyncio.run(coro)


def make_resource(fake_transport):
    return VirtualMachines(fake_transport)


def test_list_uses_default_pagination(fake_transport):
    resource = make_resource(fake_transport)

    result = run(resource.list())

    assert result == {
        "method": "get",
        "path": "compute/v1/instances",
        "kwargs": {"params": {"_limit": 50, "_offset": 0}},
    }
    assert fake_transport.calls == [result]


def test_list_includes_optional_sort_and_expand(fake_transport):
    resource = make_resource(fake_transport)

    run(resource.list(limit=10, offset=20, sort="name:asc", expand=["image", "machine_type"]))

    assert fake_transport.calls == [
        {
            "method": "get",
            "path": "compute/v1/instances",
            "kwargs": {
                "params": {
                    "_limit": 10,
                    "_offset": 20,
                    "_sort": "name:asc",
                    "expand": ["image", "machine_type"],
                }
            },
        }
    ]


@pytest.mark.parametrize(
    ("expand", "expected_params"),
    [
        (None, {}),
        (["image"], {"expand": ["image"]}),
    ],
)
def test_get_builds_params(fake_transport, expand, expected_params):
    resource = make_resource(fake_transport)

    result = run(resource.get("vm-1", expand=expand))

    assert result == {
        "method": "get",
        "path": "compute/v1/instances/vm-1",
        "kwargs": {"params": expected_params},
    }
    assert fake_transport.calls == [result]


def test_create_with_minimal_payload(fake_transport):
    resource = make_resource(fake_transport)

    run(
        resource.create(
            name="vm-1",
            image_id="img-1",
            machine_type_id="type-1",
            ssh_key_name="key-1",
        )
    )

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "/v1/instances",
            "kwargs": {
                "json": {
                    "name": "vm-1",
                    "image": {"id": "img-1"},
                    "machine_type": {"id": "type-1"},
                    "ssh_key_name": "key-1",
                }
            },
        }
    ]


def test_create_includes_optional_payload_fields(fake_transport):
    resource = make_resource(fake_transport)

    run(
        resource.create(
            name="vm-1",
            image_id="img-1",
            machine_type_id="type-1",
            ssh_key_name="key-1",
            availability_zone="br-se1-a",
            user_data="#!/bin/sh",
            network={"id": "net-1"},
        )
    )

    assert fake_transport.calls[0]["kwargs"]["json"] == {
        "name": "vm-1",
        "image": {"id": "img-1"},
        "machine_type": {"id": "type-1"},
        "ssh_key_name": "key-1",
        "availability_zone": "br-se1-a",
        "user_data": "#!/bin/sh",
        "network": {"id": "net-1"},
    }


@pytest.mark.parametrize("delete_public_ip", [False, True])
def test_delete_sends_delete_public_ip_param(fake_transport, delete_public_ip):
    resource = make_resource(fake_transport)

    assert run(resource.delete("vm-1", delete_public_ip=delete_public_ip)) is None

    assert fake_transport.calls == [
        {
            "method": "delete",
            "path": "compute/v1/instances/vm-1",
            "kwargs": {"params": {"delete_public_ip": delete_public_ip}},
        }
    ]


@pytest.mark.parametrize("action", ["start", "stop", "reboot", "suspend"])
def test_actions_post_to_action_endpoints(fake_transport, action):
    resource = make_resource(fake_transport)

    assert run(getattr(resource, action)("vm-1")) is None

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": f"compute/v1/instances/vm-1/{action}",
            "kwargs": {},
        }
    ]


def test_rename_patches_rename_endpoint(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.rename("vm-1", "new-name")) is None

    assert fake_transport.calls == [
        {
            "method": "patch",
            "path": "compute/v1/instances/vm-1/rename",
            "kwargs": {"json": {"name": "new-name"}},
        }
    ]


def test_retype_posts_machine_type_payload(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.retype("vm-1", "type-2")) is None

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "compute/v1/instances/vm-1/retype",
            "kwargs": {"json": {"machine_type": {"id": "type-2"}}},
        }
    ]
