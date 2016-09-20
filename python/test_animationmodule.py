import unittest
from unittest.mock import MagicMock
from testcode import AnimationModule, InjectMicrobitModule
from Image import Image

class TestAnimationModule(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockMicrobitModule = MagicMock();
        InjectMicrobitModule(self.mockMicrobitModule)

        self.animationModule = AnimationModule();

    def test_setAllPixelsCallsImageWithAllPixelsSet(self):
        self.animationModule.SetAllPixels();
        assert self.mockMicrobitModule.show.call_args[0][0].data == '99999:99999:99999:99999:99999' 


if __name__ == '__main__':

    unittest.main()