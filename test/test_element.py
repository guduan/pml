
import unittest
import mock
from pml import element
from pml import pvs


class ElementTest(unittest.TestCase):

    def setUp(self):
        self.dev = element.Device('dev', 'dev')
        self.dev.category = 'DRIFT'
        self.el = element.Element(1, 2, 'name', 'DRIFT')
        self.el.add_device(self.dev)

    def test_element_has_s_as_attribute(self):
        self.assertEqual(self.el.s, 1)

    def test_element_has_dev_as_attribute(self):
        get_mock = mock.MagicMock()
        set_mock = mock.MagicMock()
        self.dev.get = get_mock
        self.dev.set = set_mock
        self.el.dev
        get_mock.assert_called_with()
        self.el.dev = 1
        set_mock.assert_called_with(1)

    def test_get_devices_with_no_category_gets_all(self):
        devs = self.el.get_devices()
        self.assertSequenceEqual(list(devs), [self.dev])

    def test_get_devices_with_wrong_category_gets_none(self):
        devs = self.el.get_devices('dummy')
        self.assertSequenceEqual(list(devs), [])

    def test_get_devices_with_right_category_gets_one(self):
        devs = self.el.get_devices('DRIFT')
        self.assertSequenceEqual(list(devs), [self.dev])


class DeviceTest(unittest.TestCase):

    def setUp(self):
        self.mock_get = mock.MagicMock()
        pvs.get_live = self.mock_get
        self.mock_put = mock.MagicMock()
        pvs.put_live = self.mock_put
        self.el = element.Element(1, 2, 'name', 'DRIFT')
        self.d = element.Device('dev', 'dev')
        self.d.element = self.el
        self.d.readback_pv = 'rpv'
        self.d.setpoint_pv = 'spv'

    def test_get_calls_pvs_get_live(self):
        self.d.get()
        self.mock_get.assert_called_with('rpv')

    def test_put_calls_pvs_put_live(self):
        self.d.put(1)
        self.mock_put.assert_called_with('spv', 1)

if __name__ == '__main__':
    unittest.main()
