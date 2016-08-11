import unittest
from unittest.mock import MagicMock
from code import App


class TestMainApp(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockMicrobitModule = MagicMock();
        self.mockfactory = MagicMock();
        self.app = App(self.mockfactory)
        
    def test_CallingTheAppRunModuleRequestsGame1Controller(self):
        self.app.Run(self.mockMicrobitModule)
        self.mockfactory.CreateGame.assert_called_with(1)

    # Event trigger: button A

    def test_ButtonAPressRequestsSecondGameController(self):
        mockGame = MagicMock();
        self.app.Run(self.mockMicrobitModule)
        self.app.ButtonA();
        self.mockfactory.CreateGame.assert_called_with(2)

    def test_ButtonAGameRequestsLoopRound(self):
        mockGame = MagicMock();
        self.app.Run(self.mockMicrobitModule)
        self.app.ButtonA();
        self.mockfactory.reset_mock()
        self.app.ButtonA();
        self.mockfactory.CreateGame.assert_called_with(1)
        
    # Event trigger: shake

    def test_ShakeEventCallsGameTurnFunction(self):
        mockGame = MagicMock();
        self.mockfactory.CreateGame = MagicMock(return_value=mockGame)
        self.app.Run(self.mockMicrobitModule)
        self.app.Shake();
        mockGame.Turn.assert_called_with()

if __name__ == '__main__':

    unittest.main()