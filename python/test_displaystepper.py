import unittest
from unittest.mock import MagicMock
from code import DisplayStepper


class TestDisplayStepper(unittest.TestCase):

    # Setup

    def setUp(self):
        #self.mockMicrobitModule = MagicMock();
        #self.mockfactory = MagicMock();
        self.ds = DisplayStepper()
        
    def test_OnInitialisationXYIs00(self):
        self.assertEqual(0,self.ds.X)


if __name__ == '__main__':

    unittest.main()