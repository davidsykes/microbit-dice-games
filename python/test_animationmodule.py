import unittest
from unittest.mock import MagicMock
from code import AnimationModule

class TestAnimationModule(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockMicrobitModule = MagicMock();
        self.animationModule = AnimationModule(self.mockMicrobitModule);

    def test_setAllPixelsCallsImageWithAllPixelsSet(self):
        self.animationModule.SetAllPixels();
        print(self.mockMicrobitModule.mock_calls)
        self.mockMicrobitModule.ShowImage.assert_called_with('99999:99999:99999:99999:99999')


if __name__ == '__main__':

    unittest.main()