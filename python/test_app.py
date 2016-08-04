import unittest
from unittest.mock import MagicMock
from code import App


class TestMainApp(unittest.TestCase):

    # Setup

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

        
    # Event triggers

    def test_shakeEventCallsGameTurnFunction(self):
        mockGame = MagicMock();
        self.mockfactory.CreateGame = MagicMock(return_value=mockGame)
        self.app.Run(self.mockmicrobit, self.mockfactory)
        self.app.Shake();
        mockGame.Turn.assert_called_with()

if __name__ == '__main__':

    unittest.main()