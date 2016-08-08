import unittest
from unittest.mock import MagicMock
from code import AnimationModule

class TestAnimationModule(unittest.TestCase):

    # Setup

    #def setUp(self):
    #    self.mockfactory = MagicMock();
    #    self.mockAnimationModule = MagicMock()
    #    self.mockfactory.GetAnimationModule = MagicMock(return_value=self.mockAnimationModule)
    #    self.game = Game1(self.mockfactory)
        
    def test_game1InitialiseRequestsAnimationModule(self):
        #self.mockfactory.GetAnimationModule.assert_called_with()
        pass
        
    def test_gameTurnFunctionCallsSparkleAnimationFor2Seconds(self):
        #self.game.Turn()
        #self.mockAnimationModule.Sparkle.assert_called_with(2)
        pass

if __name__ == '__main__':

    unittest.main()