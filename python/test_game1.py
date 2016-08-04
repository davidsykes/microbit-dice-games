import unittest
from unittest.mock import MagicMock
from code import App
from code import Game1

class TestGame1(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockfactory = MagicMock();
        self.mockAnimationModule = MagicMock()
        self.mockfactory.GetAnimationModule = MagicMock(return_value=self.mockAnimationModule)
        self.game = Game1(self.mockfactory)
        #self.mockmicrobit = MagicMock();
        
    def test_game1InitialiseRequestsAnimationModule(self):
        self.mockfactory.GetAnimationModule.assert_called_with()
        
    def test_gameTurnFunctionCallsSparkleAnimationFor2Seconds(self):
        self.game.Turn()
        self.mockAnimationModule.Sparkle.assert_called_with(2)

if __name__ == '__main__':

    unittest.main()