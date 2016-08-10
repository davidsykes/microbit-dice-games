from microbit import *

#################### microbitapi.py ####################

class MicrobitApi:
    def Image(self, image):
        display.show(image);
    def Random(self, start, end):
        return randint(start, end)
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
        self.microbitModule.Show(number)

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
    def Run(self, microbit, factory):
        microbit.Image(Image.HEART)
        self.gameController = factory.CreateGame(1)
        
    def Shake(self):
        self.gameController.Turn()

###  main.py ###

if __name__ == '__main__':
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
        if accelerometer.was_gesture("shake"):
            app.Shake();
