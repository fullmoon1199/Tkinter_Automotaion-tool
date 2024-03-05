def colorcode(a):
    if a == "\x1b[0;31m":
        return 'red'
    if a == "\x1b[0;32m":
        return 'green'
    if a == "\x1b[0;33m":
        return 'yellow'
    if a == "\x1b[0;34m":
        return 'blue'
    if a == "\x1b[0;35":
        return 'purple'
    if a == "\x1b[0;36m":
        return 'cyan'
    if a == "\x1b[0;37m":
        return 'white'