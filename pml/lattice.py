

class Lattice(object):
    """
    A sequence of elements, which may represent a ring.
    """

    def __init__(self):
        self._elements = []

    def __len__(self):
        return len(self._elements)

    def __str__(self):
        return 'Lattice object with {} elements'.format(len(self))

    def get_element(self, i):
        return self._elements[i]

    def get_elements(self, group=None, category=None):
        if category is None and group is None:
            return self._elements
        elif group is not None:
            elements = []
            for element in self._elements:
                if element.is_in_group(group):
                    elements.append(element)
            return elements
        else:
            elements = []
            for element in self._elements:
                devices = element.get_devices(category)
                if devices:
                    elements.append(element)
            return elements

    def append(self, element):
        self._elements.append(element)
