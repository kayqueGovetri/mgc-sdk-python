import asyncio

import pytest

from src.mgc.resources.compute.snapshots import Snapshots


def run(coro):
    return asyncio.run(coro)


def make_resource(fake_transport):
    return Snapshots(fake_transport)


def test_list_uses_default_pagination(fake_transport):
    resource = make_resource(fake_transport)

    result = run(resource.list())
    assert result == {
        "method": "get",
        "path": "compute/v1/snapshots",
        "kwargs": {"params": {"_limit": 50, "_offset": 0}},
    }
    assert fake_transport.calls == [result]


def test_list_includes_optional_sort_and_expand(fake_transport):
    resource = make_resource(fake_transport)

    run(resource.list(limit=10, offset=20, sort="name:asc", expand=["instance"]))

    assert fake_transport.calls == [
        {
            "method": "get",
            "path": "compute/v1/snapshots",
            "kwargs": {"params": {"_limit": 10, "_offset": 20, "_sort": "name:asc", "expand": ["instance"]}},
        }
    ]


@pytest.mark.parametrize(
    ("expand", "expected_params"),
    [
        (None, {}),
        (["instance"], {"expand": ["instance"]}),
    ],
)
def test_get_builds_params(fake_transport, expand, expected_params):
    resource = make_resource(fake_transport)

    result = run(resource.get("snap-1", expand=expand))
    assert result == {
        "method": "get",
        "path": "compute/v1/snapshots/snap-1",
        "kwargs": {"params": expected_params},
    }
    assert fake_transport.calls == [result]


def test_create_with_instance_id_only(fake_transport):
    resource = make_resource(fake_transport)

    run(resource.create(instance_id="vm-1"))

    assert fake_transport.calls == [
        {"method": "post", "path": "compute/v1/snapshots", "kwargs": {"json": {"instance_id": "vm-1"}}}
    ]


def test_create_includes_optional_name_and_description(fake_transport):
    resource = make_resource(fake_transport)

    run(resource.create(instance_id="vm-1", name="snap-1", description="description"))

    assert fake_transport.calls == [
        {
            "method": "post",
            "path": "compute/v1/snapshots",
            "kwargs": {"json": {"instance_id": "vm-1", "name": "snap-1", "description": "description"}},
        }
    ]


def test_delete_deletes_snapshot(fake_transport):
    resource = make_resource(fake_transport)

    assert run(resource.delete("snap-1")) is None
    assert fake_transport.calls == [{"method": "delete", "path": "compute/v1/snapshots/snap-1", "kwargs": {}}]


@pytest.mark.parametrize(
    ("instance_id", "expected_json"),
    [
        (None, {}),
        ("vm-1", {"instance_id": "vm-1"}),
    ],
)
def test_restore_builds_optional_instance_payload(fake_transport, instance_id, expected_json):
    resource = make_resource(fake_transport)

    run(resource.restore("snap-1", instance_id=instance_id))

    assert fake_transport.calls == [
        {"method": "post", "path": "compute/v1/snapshots/snap-1/restore", "kwargs": {"json": expected_json}}
    ]


@pytest.mark.parametrize(
    ("name", "expected_json"),
    [
        (None, {"instance_id": "vm-1"}),
        ("snap-1", {"instance_id": "vm-1", "name": "snap-1"}),
    ],
)
def test_create_from_instance_builds_payload(fake_transport, name, expected_json):
    resource = make_resource(fake_transport)

    run(resource.create_from_instance(instance_id="vm-1", name=name))

    assert fake_transport.calls == [
        {"method": "post", "path": "compute/v1/snapshots", "kwargs": {"json": expected_json}}
    ]
