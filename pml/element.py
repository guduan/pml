from pml import pvs
from pml import units
import enum


class ElementType(enum.Enum):
    DRIFT = 0
    DIPOLE = 1
    QUAD = 2
    SEXT = 3


class Element(object):
    """
    An element corresponds to one physical or virtual object in the ring,
    which may have more than one device.  Each device is available through
    a field on the element.
    """
    def __init__(self, s, length, name, element_type):
        self.s = s
        self.length = length
        self.name = name

        self.element_type = ElementType[element_type]

        self.cell = None
        self.girder = None

        self.virtual = False

        self._devices = {}

    def __str__(self):
        return 'Element {} at s={} with {} devices'.format(self.name, self.s, len(self._devices))

    def is_type(self, element_type):
        """
        Return True if either the string or enum matching the element type
        is provided.
        """
        try:
            element_type = ElementType[element_type]
        except KeyError:
            pass
        return element_type == self.element_type

    def add_device(self, device):
        self._devices[device.field_name] = device

    def get_devices(self, family=None):
        if family is None:
            return self._devices.values()
        else:
            return [d for d in self._devices.values() if d.is_in_family(family)]

    def __getattr__(self, name):
        """
        Return value from device if present.  Note that __getattr__ has low
        priority so this will not be called if an instance variable has this
        name.
        """
        return self._devices[name].get()

    def __setattr__(self, name, value):
        if '_devices' in self.__dict__ and name in self.__dict__['_devices']:
            self.__dict__['_devices'][name].set(value)
        else:
            object.__setattr__(self, name, value)


class Device(object):
    """
    A device corresponds to one value on one element, with readback and
    possibly setpoint PVs.  This is controlled by PVs and may have both
    hardware and physics units.

    A device may be a member of zero or more families.
    """
    def __init__(self, name, field_name, rb=None, sp=None):
        self.name = name
        self.field_name = field_name
        self.readback_pv = rb
        self.setpoint_pv = sp
        self.conv = units.Conversion()
        self._families = set()

    def add_to_family(self, family):
        self._families.add(family)

    def is_in_family(self, family):
        return family in self._families

    def get(self, physics=False):
        hw_value = pvs.get_live(self.readback_pv)
        if physics:
            return self.conv.to_phys(hw_value)
        else:
            return hw_value

    def put(self, value, physics=False):
        if physics:
            value = self.conv.to_hw(value)
        pvs.put_live(self.setpoint_pv, value)
