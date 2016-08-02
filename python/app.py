

class App:
    def Run(self, microbit, factory):
        microbit.Image(1)
        self.gameController = factory.CreateGame(1)
        
    def Shake(self):
        self.gameController.Turn()