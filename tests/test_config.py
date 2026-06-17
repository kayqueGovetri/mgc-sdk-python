from dataclasses import FrozenInstanceError

import pytest

from src.mgc.config import ClientConfig
from src.mgc.region import Region


def test_client_config_defaults():
    config = ClientConfig()

    assert config.region == Region.BR_SE1
    assert config.timeout == 30.0


def test_client_config_accepts_custom_values():
    config = ClientConfig(region=Region.BR_NE1, timeout=10.5)

    assert config.region == Region.BR_NE1
    assert config.timeout == 10.5


def test_client_config_is_frozen():
    config = ClientConfig()

    with pytest.raises(FrozenInstanceError):
        config.timeout = 1.0


def test_client_config_uses_slots():
    config = ClientConfig()

    assert not hasattr(config, "__dict__")
