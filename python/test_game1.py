import unittest
from unittest.mock import MagicMock
from testcode import App, InjectMicrobitModule, SetRandom
from testcode import Game1

class TestGame1(unittest.TestCase):

    # Setup

    def setUp(self):
        self.mockfactory = MagicMock();

        self.mockAnimationModule = MagicMock()
        self.mockfactory.GetAnimationModule = MagicMock(return_value=self.mockAnimationModule)

        self.mockMicrobitModule = MagicMock()
        InjectMicrobitModule(self.mockMicrobitModule)

        self.mockRandomModule = MagicMock()
        SetRandom(self.mockRandomModule)

        self.game = Game1(self.mockfactory)

    # Initialise
        
    def test_game1InitialiseRequestsAnimationModule(self):
        self.mockfactory.GetAnimationModule.assert_called_with()
        
    def test_game1InitialiseDisplaysAnImage(self):
        self.mockMicrobitModule.show.assert_called_with('Heart')

    # Turn
        
    def test_gameTurnFunctionCallsSparkleAnimationFor2Seconds(self):
        self.game.Turn()
        self.mockAnimationModule.Sparkle.assert_called_with(2)

    def test_gameTurnFunctionFetchesRandomNumber1To6(self):
        self.game.Turn()
        self.mockRandomModule.randint.assert_called_with(1,6)

    def test_gameTurnFunctionDisplaysResultOfRandomCallAsString(self):
        self.mockRandomModule.randint = MagicMock(return_value=42)
        self.game.Turn()
        self.mockMicrobitModule.show.assert_called_with('42')

if __name__ == '__main__':

    unittest.main()