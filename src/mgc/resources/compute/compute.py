from .backups import Backups
from .images import Images
from .machine_types import MachineTypes
from .snapshots import Snapshots
from .virtual_machines import VirtualMachines


class Compute:
    """Namespace for Magalu Cloud compute resources."""

    def __init__(self, transport):
        """Create compute resource clients that share the same transport.

        Args:
            transport: Transport used by all compute resource clients.
        """
        self.virtual_machines = VirtualMachines(transport)
        self.images = Images(transport)
        self.machine_types = MachineTypes(transport)
        self.snapshots = Snapshots(transport)
        self.backups = Backups(transport)
