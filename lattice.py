

class Lattice(object):
    """
    A sequence of elements, which may represent a ring.
    """

    def __init__(self):
        self.elements = []

    def get_element(self, i):
        return self.elements[i]

    def get_elements(self, pattern=None):
        if pattern is None:
            return self.elements
        else:
            elements = []
            for element in self.elements:
                for device in element.devices:
                    if device.category == pattern:
                        elements.append(element)
            return elements

    def append(self, element):
        self.elements.append(element)
