

def scroll(message):
    print ('Scroll:', message)
    
def show(image):
    print ('Image:', image, type(image))
    if not (type(image) is str):
        raise Exception('Show must be string or image')
    
def sleep(time):
    print ('Sleep:', time)
