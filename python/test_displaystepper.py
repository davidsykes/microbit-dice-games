import unittest
from unittest.mock import MagicMock
from code import DisplayStepper


class TestDisplayStepper(unittest.TestCase):

    # Setup

    def setUp(self):
        self.ds = DisplayStepper()
        
    def test_firstCallToNextReturnsTrue(self):
        self.assertTrue(self.ds.Next())

    def test_firstCallToNextStartsWith0(self):
        self.ds.Next()
        self.assertEqual(0,self.ds.X)
        self.assertEqual(0,self.ds.Y)

    def test_Call2ToNextMovesTo10(self):
        for _ in range(2):
            self.ds.Next()
        self.assertEqual(1,self.ds.X)
        self.assertEqual(0,self.ds.Y)

    def test_Call3ToNextMovesTo20(self):
        for _ in range(3):
            self.ds.Next()
        self.assertEqual(2,self.ds.X)
        self.assertEqual(0,self.ds.Y)

    def test_Call6ToNextMovesTo01(self):
        for _ in range(6):
            self.ds.Next()
        self.assertEqual(0,self.ds.X)
        self.assertEqual(1,self.ds.Y)

    def test_Call11ToNextMovesTo02(self):
        for _ in range(11):
            self.ds.Next()
        self.assertEqual(0,self.ds.X)
        self.assertEqual(2,self.ds.Y)

    def test_Call25ToNextMovesTo44(self):
        for _ in range(25):
            self.ds.Next()
        self.assertEqual(4,self.ds.X)
        self.assertEqual(4,self.ds.Y)

    def test_Call25ToNextReturnsTrue(self):
        for _ in range(24):
            self.ds.Next()
        self.assertTrue(self.ds.Next())
        
    def test_Call26ToNextReturnsFalse(self):
        for _ in range(25):
            self.ds.Next()
        self.assertFalse(self.ds.Next())
        


if __name__ == '__main__':

    unittest.main()