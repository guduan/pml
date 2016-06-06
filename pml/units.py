


class NullConversion(object):

    def __init__(self):
        self.hw_units = ''
        self.phys_units = ''

    def to_phys(self, hw_value):
        return hw_value

    def to_hw(self, phys_value):
        return phys_value
