import unittest
from unittest.mock import MagicMock
from code import App
from code import Game2

class TestGame2(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockfactory = MagicMock();

        self.mockAnimationModule = MagicMock()
        self.mockfactory.GetAnimationModule = MagicMock(return_value=self.mockAnimationModule)

        self.mockMicrobitModule = MagicMock()
        self.mockfactory.GetMicrobitModule = MagicMock(return_value=self.mockMicrobitModule)

        self.game = Game2(self.mockfactory)

    # Initialise
        
    def test_game2InitialiseRequestsMicrobitModule(self):
        self.mockfactory.GetMicrobitModule.assert_called_with()
        
    def test_game2InitialiseDisplaysR(self):
        self.mockMicrobitModule.Show.assert_called_with('R')
    
    # Turn

    def test_gameTurnFunctionSetsAllPixelsOn(self):
        self.mockAnimationModule.reset_mock()
        self.game.Turn()
        self.mockAnimationModule.SetAllPixels.assert_called_with()
        
    # Polling

    def test_gameDoesNothingUntilTurnReceived(self):
        self.mockMicrobitModule.RunningTime = MagicMock(return_value=12345678)
        self.game.Poll()
        self.mockAnimationModule.SetAllPixels.assert_not_called()
        self.mockAnimationModule.SetPixel.assert_not_called()

    def test_gameDoesNothingBeforeFirstTimePeriod(self):
        self.mockMicrobitModule.RunningTime = MagicMock(return_value=1234)
        self.game.Turn()
        self.mockMicrobitModule.RunningTime = MagicMock(return_value=1234 + self.game.TimePeriod - 1)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_not_called()

    def test_gameClearsFirstPixelOnFirstTimePeriod(self):
        self.mockMicrobitModule.RunningTime = MagicMock(return_value=1234)
        self.game.Turn()
        self.mockMicrobitModule.RunningTime = MagicMock(return_value=1234 + self.game.TimePeriod)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_called_with(0,0,0)

if __name__ == '__main__':
    unittest.main()