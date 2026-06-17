import asyncio

from src.mgc.resources.compute.images import Images


def run(coro):
    return asyncio.run(coro)


def test_list_uses_default_pagination(fake_transport):
    resource = Images(fake_transport)

    result = run(resource.list())

    assert result == {
        "method": "get",
        "path": "compute/v1/images",
        "kwargs": {"params": {"_limit": 50, "_offset": 0}},
    }
    assert fake_transport.calls == [result]


def test_list_includes_optional_sort_and_expand(fake_transport):
    resource = Images(fake_transport)

    run(resource.list(limit=10, offset=20, sort="name:asc", expand=["os"]))

    assert fake_transport.calls == [
        {
            "method": "get",
            "path": "compute/v1/images",
            "kwargs": {"params": {"_limit": 10, "_offset": 20, "_sort": "name:asc", "expand": ["os"]}},
        }
    ]
