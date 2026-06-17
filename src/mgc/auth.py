from abc import ABC, abstractmethod


class AuthProvider(ABC):
    """Define the interface for SDK authentication providers."""

    @abstractmethod
    def get_access_token(self) -> str:
        """Return authentication data used to authorize SDK requests."""
        raise NotImplementedError
