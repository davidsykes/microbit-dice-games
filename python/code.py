from microbit import *

### microbitapi.py ###

class MicrobitApi:
    def Image(self, image):
        display.show(image);

### game1.py ###

class Game:
    def Turn(self):
        display.scroll('turn')

class Game1:
    def __init__(self, factory):
        self.animationModule = factory.GetAnimationModule()
        
    def Turn(self):
        self.animationModule.Sparkle(2)

### factory.py ###

class Factory:
    def CreateGame(self, num):
        return Game()

################### App ############################

class App:
    def Run(self, microbit, factory):
        microbit.Image(Image.HEART)
        self.gameController = factory.CreateGame(1)
        
    def Shake(self):
        self.gameController.Turn()

###  main.py ###

mbapi = MicrobitApi()
fac = Factory();
app = App()
display.scroll('!')
app.Run(mbapi, fac)

while True:
    if button_a.is_pressed():
        mbapi.Image(Image.SMILE);
        while button_a.is_pressed():
            pass
        app.Shake();