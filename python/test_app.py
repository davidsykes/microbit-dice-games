import unittest
from unittest.mock import MagicMock
from app import App


class TestMainApp(unittest.TestCase):

    def setUp(self):

        self.app = App()
        
    def test_callingTheAppRunModuleDisplaysAnImage(self):
        mockmicrobit = MagicMock();
        self.app.Run(mockmicrobit)
        mockmicrobit.Image.assert_called_with(1)

if __name__ == '__main__':

    unittest.main()