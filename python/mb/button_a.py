from keyboard import CheckKeyboard


def is_pressed():
    current = CheckKeyboard(True)
    if current & 1:
        print 'Button A'
    return current & 1

