import unittest
from pml import lattice
from pml import element


class TestLattice(unittest.TestCase):

    def setUp(self):
        self.lattice = lattice.Lattice()
        self.drift = element.Element(1, 2, 'name', 'DRIFT')
        self.lattice.append(self.drift)
        self.quad = element.Element(2, 3, 'name2', 'QUAD')
        self.dev0 = element.Device('dev_name', 'dev')
        self.dev0.add_to_family('dev_family')
        self.quad.add_device(self.dev0)
        self.lattice.append(self.quad)

    def test_lattice_len(self):
        self.assertEqual(len(self.lattice), 2)

    def test_get_elements_returns_element_for_string_type(self):
        els = self.lattice.get_elements('DRIFT')
        self.assertEqual(els, [self.drift])

    def test_get_elements_returns_empty_list_if_no_matches(self):
        els = self.lattice.get_elements(family='empty_family')
        self.assertEqual(els, [])

    def test_get_elements_returns_matching_element(self):
        els = self.lattice.get_elements(family='dev_family')
        self.assertEqual(els, [self.quad])

    def test_get_elements_returns_all_elements_if_no_argument(self):
        els = self.lattice.get_elements()
        self.assertEqual(len(els), 2)
        self.assertTrue(self.drift in els)
        self.assertTrue(self.quad in els)

    def test_get_element_gets_selected_element(self):
        el = self.lattice.get_element(0)
        self.assertEqual(el, self.drift)
        el = self.lattice.get_element(-1)
        self.assertEqual(el, self.quad)


if __name__ == '__main__':
    unittest.main()
