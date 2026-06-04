from .backups import Backups
from .images import Images
from .machine_types import MachineTypes
from .snapshots import Snapshots
from .virtual_machines import VirtualMachines


class Compute:
    def __init__(self, transport):
        self.virtual_machines = VirtualMachines(transport)
        self.images = Images(transport)
        self.machine_types = MachineTypes(transport)
        self.snapshots = Snapshots(transport)
        self.backups = Backups(transport)