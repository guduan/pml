from __future__ import division
import unittest

from pml import units


class TestPolyConversion(unittest.TestCase):

    def test_identity_conversion(self):
        ident_conv = units.LinearConversion(0, 1)
        for x in -1, 0.34, 7:
            self.assertEqual(x, ident_conv.to_hw(x))
            self.assertEqual(x, ident_conv.to_phys(x))

    def test_linear_conversion(self):
        ident_conv = units.LinearConversion(2, 3)
        for x in -1, 0.34, 7:
            self.assertEqual(3 * x + 2, ident_conv.to_hw(x))
            self.assertEqual(((x - 2) / 3), ident_conv.to_phys(x))


if __name__ == '__main__':
    unittest.main()
