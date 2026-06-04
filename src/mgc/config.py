from dataclasses import dataclass

from .region import Region


@dataclass(slots=True, frozen=True)
class ClientConfig:
    region: str = Region.BR_SE1
    timeout: float = 30.0
