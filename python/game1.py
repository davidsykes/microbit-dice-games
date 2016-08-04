

class Game:
    def Turn(self):
        display.scroll('turn')

class Game1:
    def __init__(self, factory):
        self.animationModule = factory.GetAnimationModule()
        
    def Turn(self):
        self.animationModule.Sparkle(2)
