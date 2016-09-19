from microbit import *
import random

#################### Random module ####################

class RandomImp:
    def randint(self,p1,p2):
        return random.randint(p1,p2)

randomModule = RandomImp()

def SetRandom(r):
    global randomModule
    randomModule = r

#################### AnimationModule ####################

class AnimationModule:
    def SetAllPixels(self):
        display.show(Image('99999:99999:99999:99999:99999'))

    def SetPixel(self, x, y, v):
        display.set_pixel(x,y,v);

    def Sparkle(self, time):
        display.scroll('?')

#################### DisplayStepper #################### 
        
class DisplayStepper:
    X = 4
    Y = -1
    def Next(self):
        self.X = self.X + 1
        if self.X > 4:
            self.X = 0
            self.Y = self.Y + 1

#################### game1 #################### 

class Game1:
    def __init__(self, factory):
        self.animationModule = factory.GetAnimationModule()
        display.show(Image.HEART)
        
    def Turn(self):
        self.animationModule.Sparkle(2)
        number = randomModule.randint(1,6)
        display.show(str(number))
        
    def Poll(self):
        pass

#################### game2 #################### 

class Game2:
    TimePeriod = 2400

    def __init__(self, factory):
        self.animationModule = factory.GetAnimationModule()
        self.time = 0
        display.show('R')
        self.displayStepper = DisplayStepper() 
        
    def Turn(self):
        self.animationModule.SetAllPixels()
        self.time = running_time()
        
    def Poll(self):
        if (self.time > 0) and (running_time() >= (self.time + self.TimePeriod)):
            self.time = self.time + self.TimePeriod
            self.displayStepper.Next()
            self.animationModule.SetPixel(self.displayStepper.X,self.displayStepper.Y,0)

#################### factory.py #########################

class Factory:
    def CreateGame(self, num):
        if num == 2:
            return Game2(self)
        return Game1(self)
    def GetAnimationModule(self):
        return AnimationModule()

################### App ############################

class App:
    def __init__(self, factory):
        self.factory = factory
        self.nextGame = 1

    def Run(self):
        self.gameController = self.factory.CreateGame(self.nextGame)
    
    def ButtonA(self):
        self.nextGame = self.nextGame + 1 if self.nextGame < 2 else 1
        self.gameController = self.factory.CreateGame(self.nextGame)
        
    def Shake(self):
        self.gameController.Turn()
        
    def Poll(self):
        self.gameController.Poll()

###  main.py ###

if __name__ == '__main__':
    fac = Factory();
    app = App(fac)
    app.Run()

    while True:
        if button_a.is_pressed():
            app.ButtonA()
            while button_a.is_pressed():
                pass
        if accelerometer.was_gesture("shake"):
            app.Shake();
        app.Poll()
