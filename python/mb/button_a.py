from keyboard import CheckKeyboard


def is_pressed():
    current = CheckKeyboard()
    #if current:
    #    print 'Current=>', str(current)
    return current & 1

