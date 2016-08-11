from microbit import *
import random

#################### microbitapi.py ####################

class MicrobitApi:
    def Image(self, image):
        display.show(image);
    def Random(self, start, end):
        return random.randint(start, end)
    def Show(self, value):
        display.show(value)

#################### AnimationModule ####################

class AnimationModule:
    def Sparkle(self, time):
        display.scroll('xx')

#################### game1.py #################### 

class Game1:
    def __init__(self, factory):
        self.animationModule = factory.GetAnimationModule()
        self.microbitModule = factory.GetMicrobitModule()
        
    def Turn(self):
        self.animationModule.Sparkle(2)
        number = self.microbitModule.Random(1,6)
        self.microbitModule.Show(str(number))

#################### factory.py #########################

class Factory:
    def CreateGame(self, num):
        return Game1(self)
    def GetAnimationModule(self):
        return AnimationModule()
    def GetMicrobitModule(self):
        return MicrobitApi()

################### App ############################

class App:
    def __init__(self, factory):
        self.factory = factory
        self.nextGame = 1

    def Run(self, microbit):
        microbit.Image(Image.HEART)
        self.gameController = self.factory.CreateGame(self.nextGame)
    
    def ButtonA(self):
        self.nextGame = self.nextGame + 1 if self.nextGame < 2 else 1
        self.gameController = self.factory.CreateGame(self.nextGame)
        
    def Shake(self):
        self.gameController.Turn()

###  main.py ###

if __name__ == '__main__':
    mbapi = MicrobitApi()
    fac = Factory();
    app = App()
    app.Run(mbapi, fac)

    while True:
        if button_a.is_pressed():
            mbapi.Image(Image.SMILE);
            while button_a.is_pressed():
                pass
            app.Shake();
        if accelerometer.was_gesture("shake"):
            app.Shake();
