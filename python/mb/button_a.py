
current = 0

def is_pressed():
    global current
    current = int(raw_input("?"))
    print 'Current=>', str(current)
    return current & 1

