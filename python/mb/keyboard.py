#!/usr/bin/env python

import sys, termios, atexit
from select import select

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def putch(ch):
    sys.stdout.write(ch)

def getch():
    return sys.stdin.read(1)

def getche():
    ch = getch()
    putch(ch)
    return ch

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    return dr <> []

class KeyboardLinux:
	def __init__(self):
		atexit.register(set_normal_term)
		set_curses_term()

	def kbhit(self):
		return kbhit()

	def getch(self):
		return getch()

	def GetByte(self):
		if self.kbhit():
			return self.getch()
		return None


kb = KeyboardLinux()

current = 0

def CheckKeyboard(firstCallInLoopChecksForNewKey):
	global current
	if firstCallInLoopChecksForNewKey:
		current = 0
		pressed = kb.kbhit()
		if pressed:
			ch = kb.getch()
			if ch.isdigit():
				current = int(ch)
	return current
