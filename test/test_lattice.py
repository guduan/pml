
import unittest
from pml import lattice
from pml import element

class TestLattice(unittest.TestCase):

    def setUp(self):
        self.lattice = lattice.Lattice()
        self.el0 = element.Element(1, 2, 'name')
        self.lattice.append(self.el0)
        self.el1 = element.Element(2, 3, 'name2')
        self.dev0 = element.Device('dev_name', 'dev')
        self.dev0.category = 'cat1'
        self.el1.add_device(self.dev0)
        self.lattice.append(self.el1)

    def test_lattice_len(self):
        self.assertEqual(len(self.lattice), 2)

    def test_get_elements_returns_empty_list_if_no_matches(self):
        els = self.lattice.get_elements(category='cat0')
        self.assertEqual(els, [])

    def test_get_elements_returns_matching_element(self):
        els = self.lattice.get_elements(category='cat1')
        self.assertEqual(els, [self.el1])

    def test_get_elements_returns_all_elements_if_no_argument(self):
        els = self.lattice.get_elements()
        self.assertEqual(len(els), 2)
        self.assertTrue(self.el0 in els)
        self.assertTrue(self.el1 in els)

    def test_get_element_gets_selected_element(self):
        el = self.lattice.get_element(0)
        self.assertEqual(el, self.el0)
        el = self.lattice.get_element(-1)
        self.assertEqual(el, self.el1)


if __name__ == '__main__':
    unittest.main()
