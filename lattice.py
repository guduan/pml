

class Lattice(object):
    """
    A sequence of elements, which may represent a ring.
    """

    def __init__(self):
        self._elements = []

    def get_element(self, i):
        return self._elements[i]

    def get_elements(self, category=None):
        if category is None:
            return self._elements
        else:
            elements = []
            for element in self._elements:
                devices = element.get_devices(category)
                if devices:
                    elements.append(element)
            return elements

    def append(self, element):
        self._elements.append(element)
