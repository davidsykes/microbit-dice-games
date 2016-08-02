import unittest
from unittest.mock import MagicMock
from app import App


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.mockmicrobit = MagicMock();
        self.mockfactory = MagicMock();
        
    def test_callingTheAppRunModuleDisplaysAnImage(self):
        self.app.Run(self.mockmicrobit, self.mockfactory)
        self.mockmicrobit.Image.assert_called_with(1)
        
    def test_callingTheAppRunModuleRequestsGame1Controller(self):
        self.app.Run(self.mockmicrobit, self.mockfactory)
        self.mockfactory.CreateGame.assert_called_with(1)

if __name__ == '__main__':

    unittest.main()