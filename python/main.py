from microbit import *
from app import App
from microbitapi import MicrobitApi
from factory import Factory

mbapi = MicrobitApi()
fac = Factory();
appw = App()
display.scroll('sss')
appw.Run(mbapi, fac)