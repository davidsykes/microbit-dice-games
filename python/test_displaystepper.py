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
        self.assertEqual(0,self.ds.Y)

    def test_firstCallToNextMovesTo10(self):
        self.ds.Next()
        self.assertEqual(1,self.ds.X)
        self.assertEqual(0,self.ds.Y)

    def test_secondCallToNextMovesTo20(self):
        for _ in range(2):
            self.ds.Next()
        self.assertEqual(2,self.ds.X)
        self.assertEqual(0,self.ds.Y)

    def test_fifthCallToNextMovesTo01(self):
        for _ in range(5):
            self.ds.Next()
        self.assertEqual(0,self.ds.X)
        self.assertEqual(1,self.ds.Y)

    def test_tenthCallToNextMovesTo02(self):
        for _ in range(10):
            self.ds.Next()
        self.assertEqual(0,self.ds.X)
        self.assertEqual(2,self.ds.Y)

    def test_24thCallToNextMovesTo44(self):
        for _ in range(24):
            self.ds.Next()
        self.assertEqual(4,self.ds.X)
        self.assertEqual(4,self.ds.Y)

if __name__ == '__main__':

    unittest.main()