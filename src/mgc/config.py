from dataclasses import dataclass

from .region import Region


@dataclass(slots=True, frozen=True)
class ClientConfig:
    """Configure SDK transport options.

    Attributes:
        region: Magalu Cloud region used to build API requests.
        timeout: Request timeout in seconds.
    """

    region: str = Region.BR_SE1
    timeout: float = 30.0
