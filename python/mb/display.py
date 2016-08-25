import time
from Image import Image

def scroll(message):
    print ('Scroll:', message)
    
def show(image):
    print ('Image:', image, type(image))
    if isinstance(image, Image):
        pass
    elif not (type(image) is str):
        raise Exception('Show must be string or image')

def set_pixel(x,y,v):
    print('Set pixel', x, y, v)

def sleep(time):
    print ('Sleep:', time)

def running_time():
    return int(round(time.time() * 1000))