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

        self.mockMicrobitModule = MagicMock()
        self.mockfactory.GetMicrobitModule = MagicMock(return_value=self.mockMicrobitModule)

        self.game = Game1(self.mockfactory)
        
    def test_game1InitialiseRequestsAnimationModule(self):
        self.mockfactory.GetAnimationModule.assert_called_with()
        
    def test_game1InitialiseRequestsMicrobitModule(self):
        self.mockfactory.GetMicrobitModule.assert_called_with()
        
    def test_game1InitialiseDisplaysAnImage(self):
        self.mockMicrobitModule.Image.assert_called_with('Heart')
        
    def test_gameTurnFunctionCallsSparkleAnimationFor2Seconds(self):
        self.game.Turn()
        self.mockAnimationModule.Sparkle.assert_called_with(2)

    def test_gameTurnFunctionFetchesRandomNumber1To6(self):
        self.game.Turn()
        self.mockMicrobitModule.Random.assert_called_with(1,6)

    def test_gameTurnFunctionDisplaysResultOfRandomCallAsString(self):
        self.mockMicrobitModule.Random = MagicMock(return_value=42)
        self.game.Turn()
        self.mockMicrobitModule.Show.assert_called_with('42')

if __name__ == '__main__':

    unittest.main()