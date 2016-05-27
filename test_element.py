
import pkg_resources
pkg_resources.require('cothread')
pkg_resources.require('mock')

import unittest
import element
import mock
import pvs
pvs.get_live = mock.MagicMock()


class ElementTest(unittest.TestCase):

    def setUp(self):
        self.dev = element.Device('dev', 'dev')
        self.el = element.Element(1, 2, 'name')
        self.el.add_device(self.dev)

    def test_element_has_s_as_attribute(self):
        print(self.el.s)
        print(self.el.__dict__)
        self.assertEqual(self.el.s, 1)
        self.assertEqual(self.el.dev, 1)

    def test_element_has_dev_as_attribute(self):
        get_mock = mock.MagicMock()
        set_mock = mock.MagicMock()
        self.dev.get = get_mock
        self.dev.set = set_mock
        self.el.dev
        get_mock.assert_called_with()
        self.el.dev = 1
        set_mock.assert_called_with(1)


class DeviceTest(unittest.TestCase):

    def setUp(self):
        self.el = element.Element(1, 2, 'name')
        self.d = element.Device('dev', 'dev')
        self.d.element = self.el
        self.d.readback_pv = 'rpv'

    def test_device_gets_s_from_element(self):
        self.assertEqual(self.d.s, self.el.s)

    def test_device_gets_length_from_element(self):
        self.assertEqual(self.d.length, self.el.length)

    def test_if_live_calls_pvs_get_live(self):
        self.d.get()
        pvs.get_live.assert_called_with('rpv')

    def test_if_not_live_does_not_call_pvs_get_live(self):
        self.d.get()
        pvs.get_live.assert_never_called()


if __name__ == '__main__':
    unittest.main()
