
press = True

def is_pressed():
    global press
    pressed = press
    press = False
    return pressed

