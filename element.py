import pvs


class Element(object):
    """
    An element corresponds to one physical device in the ring, which may
    have more than one device.  Each device is available through
    a field.
    """
    def __init__(self, s, length, name):
        self.s = s
        self.length = length
        self.name = name

        self.cell = None
        self.girder = None

        self.virtual = False

        self._devices = {}

    def set_live(self, live):
        self.live = live
        for device in self._devices:
            device.set_live(live)

    def add_device(self, device):
        device.element = self
        self._devices[device.field_name] = device

    def get_devices(self, category=None):
        if category is None:
            return self._devices.values()
        else:
            return [d for d in self._devices.values() if d.category == category]

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
    possibly setpoint PVs.
    """
    def __init__(self, name, field_name):
        self.name = name
        self.field_name = field_name
        self.element = None
        self.phys_units = ''
        self.hw_units = ''
        self.readback_pv = None
        self.setpoint_pv = None
        self.conv = None
        self.live = True
        self.category = None

    def get(self, physics=False):
        # Should the live version set the model value? I think no
        hw_value = pvs.get_live(self.readback_pv)
        if physics:
            return self.conv.to_physics(hw_value)
        else:
            return hw_value

    @property
    def s(self):
        return self.element.s

    @property
    def length(self):
        return self.element.length


