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
        turnStartTime = self.StartGameTurn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime + self.game.TimePeriod - 1)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_not_called()

    def test_gameClearsFirstPixelOnFirstTimePeriod(self):
        turnStartTime = self.StartGameTurn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime + self.game.TimePeriod)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_called_once_with(0,0,0)
        assert self.mockAnimationModule.SetPixel.call_count == 1

    def test_gameClearsOnlyFirstPixelAfterASinglePollInTwoTimePeriods(self):
        turnStartTime = self.StartGameTurn()
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime + self.game.TimePeriod * 2)
        self.game.Poll()
        self.mockAnimationModule.SetPixel.assert_called_once_with(0,0,0)
        assert self.mockAnimationModule.SetPixel.call_count == 1

    def test_gameClearsTwoPixelsAfterAMultiplePollsInTwoTimePeriods(self):
        turnStartTime = self.StartGameTurn()
        self.game.Poll()
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime + self.game.TimePeriod * 2)
        self.game.Poll()
        self.game.Poll()
        assert self.mockAnimationModule.SetPixel.call_count == 2
        self.mockAnimationModule.SetPixel.assert_any_call(0,0,0)
        self.mockAnimationModule.SetPixel.assert_any_call(1,0,0)

    def test_on6thTimePeriodTheGameStartsClearingTheSecondRow(self):
        turnStartTime = self.StartGameTurn()
        self.game.Poll()
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime+self.game.TimePeriod * 6)
        for _ in range(6):
            self.game.Poll()
        assert self.mockAnimationModule.SetPixel.call_count == 6
        self.mockAnimationModule.SetPixel.assert_called_with(0,1,0)
        
    def test_on26thTimePeriodTheGameDisplaysAnX(self):
        turnStartTime = self.StartGameTurn()
        self.RunSomePlayTime(polls = 25, timeToRunTo = turnStartTime+self.game.TimePeriod * 25)
        self.mockMicrobitModule.reset_mock()
        self.RunSomePlayTime(polls = 26, timeToRunTo = turnStartTime+self.game.TimePeriod * 26)
        self.mockMicrobitModule.show.assert_called_with('Sad')
        
    def test_whenASecondTurnIsStartedTheGameSetsAllThePixelsAgain(self):
        turnStartTime = self.StartGameTurn()
        self.RunSomePlayTime(polls = 5, timeToRunTo = turnStartTime+self.game.TimePeriod * 5)
        self.mockAnimationModule.reset_mock()
        turnStartTime = self.StartGameTurn()
        self.mockAnimationModule.SetAllPixels.assert_called_once_with()
        
    def test_whenASecondTurnIsStartedTheGameResetsThePixelClearing(self):
        turnStartTime = self.StartGameTurn()
        self.RunSomePlayTime(polls = 5, timeToRunTo = turnStartTime+self.game.TimePeriod * 5)
        self.game.Turn()
        self.mockAnimationModule.reset_mock()

        self.RunSomePlayTime(polls = 1, timeToRunTo = turnStartTime+self.game.TimePeriod * 6)

        self.mockAnimationModule.SetPixel.assert_called_once_with(0,0,0)
        
    def test_whenTheTimeRunsOutTheTurnActionIsDisabled(self):
        turnStartTime = self.StartGameTurn()
        self.RunSomePlayTime(polls = 26, timeToRunTo = turnStartTime+self.game.TimePeriod * 26)
        self.mockAnimationModule.reset_mock()
        self.game.Turn()
        self.mockAnimationModule.SetAllPixels.assert_not_called()
        
    # Support code
    
    def StartGameTurn(self):
        turnStartTime = 1234
        self.mockMicrobitModule.running_time = MagicMock(return_value=turnStartTime)
        self.game.Turn()
        return turnStartTime
        
    def RunSomePlayTime(self, polls, timeToRunTo):
        self.mockMicrobitModule.running_time = MagicMock(return_value=timeToRunTo)
        for _ in range(polls):
            self.game.Poll()

if __name__ == '__main__':
    unittest.main()