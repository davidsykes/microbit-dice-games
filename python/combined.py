from microbit import *

class MicrobitApi:
    def Image(self, image):
        display.show(image);        

class Game:
    def Turn(self):
        display.scroll('turn')

class Factory:
    def CreateGame(self, num):
        return Game()

class App:
    def Run(self, microbit, factory):
        microbit.Image(Image.HEART)
        self.gameController = factory.CreateGame(1)
        
    def Shake(self):
        self.gameController.Turn()

mbapi = MicrobitApi()
fac = Factory();
appw = App()
display.scroll('sss')
appw.Run(mbapi, fac)
