import unittest
from unittest.mock import MagicMock
from testcode import App, InjectMicrobitModule
from testcode import Game2

class TestGame2(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockfactory = MagicMock();

        self.mockAnimationModule = MagicMock()
        self.mockfactory.GetAnimationModule = MagicMock(return_value=self.mockAnimationModule)

        self.mockMicrobitModule = MagicMock()
        InjectMicrobitModule(self.mockMicrobitModule)
        #self.mockfactory.GetMicrobitModule = MagicMock(return_value=self.mockMicrobitModule)

        self.game = Game2(self.mockfactory)

    # Initialise
        
    def test_game2InitialiseDisplaysR(self):
        self.mockMicrobitModule.show.assert_called_with('R')
    
    # Turn

    def test_gameTurnFunctionSetsAllPixelsOn(self):
        self.mockAnimationModule.reset_mock()
        self.game.Turn()
        self.mockAnimationModule.SetAllPixels.assert_called_once_with()
        
    # Polling

    def test_gameDoesNothingUntilTurnReceived(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=12345678)
        self.game.Poll()
        self.mockAnimationModule.SetAllPixels.assert_not_called()
        self.mockAnimationModule.SetPixel.assert_not_called()

    def test_gameDoesNothingBeforeFirstTimePeriod(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234)
        self.game.Turn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234 + self.game.TimePeriod - 1)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_not_called()

    def test_gameClearsFirstPixelOnFirstTimePeriod(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234)
        self.game.Turn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234 + self.game.TimePeriod)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_called_once_with(0,0,0)
        assert self.mockAnimationModule.SetPixel.call_count == 1

    def test_gameClearsOnlyFirstPixelAfterASinglePollInTwoTimePeriods(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234)
        self.game.Turn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234 + self.game.TimePeriod * 2)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_called_once_with(0,0,0)
        assert self.mockAnimationModule.SetPixel.call_count == 1

    def test_gameClearsTwoPixelsAfterAMultiplePollsInTwoTimePeriods(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234)
        self.game.Turn()
        self.game.Poll()
        self.mockMicrobitModule.running_time = MagicMock(return_value=1234 + self.game.TimePeriod * 2)
        self.game.Poll()
        self.game.Poll()
        assert self.mockAnimationModule.SetPixel.call_count == 2
        self.mockAnimationModule.SetPixel.assert_any_call(0,0,0)
        self.mockAnimationModule.SetPixel.assert_any_call(1,0,0)

    def test_On6thTimePeriodTheGameStartsClearingTheSecondRow(self):
        self.mockMicrobitModule.running_time = MagicMock(return_value=1)
        self.game.Turn()
        self.game.Poll()
        self.mockMicrobitModule.running_time = MagicMock(return_value=1+self.game.TimePeriod * 6)
        for _ in range(6):
            self.game.Poll()
        assert self.mockAnimationModule.SetPixel.call_count == 6
        self.mockAnimationModule.SetPixel.assert_called_with(0,1,0)
        

if __name__ == '__main__':
    unittest.main()