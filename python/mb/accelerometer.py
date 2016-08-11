from keyboard import CheckKeyboard



def current_gesture():
    current = CheckKeyboard(False)
    if current:
        print 'Gesture=>', str(current)
    return 'shake' if current & 4 else ''

def was_gesture(gesture):
    current = CheckKeyboard(False)
    if current:
        print 'Gesture=>', str(current)
    return 'shake' if current & 4 else ''