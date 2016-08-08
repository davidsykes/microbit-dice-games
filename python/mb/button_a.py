from keyboard import KeyboardLinux

kb = KeyboardLinux()

current = 0

def CheckKeyboard():
    global current
    current = 0
    pressed = kb.kbhit()
    if pressed:
        ch = kb.getch()
        print 'pressed',ch.isdigit()
        if ch.isdigit():
            current = int(ch) 


def is_pressed():
    global current
    CheckKeyboard()
    if current:
        print 'Current=>', str(current)
    return current & 1

