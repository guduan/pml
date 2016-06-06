from pml import element

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

    def get_elements(self, element_type=None, category=None):
        if category is None and element_type is None:
            return self._elements
        elif element_type is not None:
            if isinstance(element_type, basestring):
                element_type = element.ElementType[element_type]
            elements = []
            for el in self._elements:
                if el.element_type == element_type:
                    elements.append(el)
            return elements
        else:
            elements = []
            for el in self._elements:
                devices = el.get_devices(category)
                if devices:
                    elements.append(el)
            return elements

    def append(self, element):
        self._elements.append(element)
