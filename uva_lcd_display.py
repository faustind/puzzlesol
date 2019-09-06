# In Oboedencia Veritas

def print_row(screen, row, col, s):
    # row, col = position of the row to print
    col = col + 1
    for i in range(s):
        screen[row][col+i] = '-'

def print_col(screen, row, col, s):
    # row, col = position of first char in the column to print
    row = row + 1
    for i in range(s):
        screen[row+i][col] = '|'

def v0(screen, top_left, s):
    print_col(screen, row=0, col=top_left, s=s)

def v1(screen, top_left, s):
    print_col(screen, row=0, col=top_left+s+1, s=s)

def v2(screen, top_left, s):
    print_col(screen, row=s+1, col=top_left, s=s)

def v3(screen, top_left, s):
    print_col(screen, row=s+1, col=top_left+s+1, s=s)


def h0(screen, top_left, s):
    print_row(screen, row=0, col=top_left, s=s)

def h1(screen, top_left, s):
    print_row(screen, row=s+1, col=top_left, s=s)

def h2(screen,top_left, s):
    print_row(screen, row=len(screen)-1, col=top_left, s=s)


def print_number(screen, s, n):
    pos = 0
    for i, d in enumerate(n):
        pos = i * (s+3)
        params = (screen, pos, s)
        if d == '0':
            h0(*params)
            h2(*params)
            v0(*params)
            v1(*params)
            v2(*params)
            v3(*params)
        elif d == '1':
            v1(*params)
            v3(*params)
        elif d == '2':
            h0(*params)
            h1(*params)
            h2(*params)
            v1(*params)
            v2(*params)
        elif d == '3':
            h0(*params)
            h1(*params)
            h2(*params)
            v1(*params)
            v3(*params)
        elif d == '4':
            v0(*params)
            v1(*params)
            v3(*params)
            h1(*params)
        elif d == '5':
            h0(*params)
            h1(*params)
            h2(*params)
            v0(*params)
            v3(*params)
        elif d == '6':
            h0(*params)
            h1(*params)
            h2(*params)
            v0(*params)
            v2(*params)
            v3(*params)
        elif d == '7':
            v1(*params)
            v3(*params)
            h0(*params)
        elif d == '8':
            h0(*params)
            h1(*params)
            h2(*params)
            v0(*params)
            v1(*params)
            v2(*params)
            v3(*params)
        else: # d == '9'
            h0(*params)
            h1(*params)
            h2(*params)
            v0(*params)
            v1(*params)
            v3(*params)


def print_screen(screen):
    for row in screen:
        for c in row:
            print(c, end='')
        print()

while True:
    s, n = input().split()
    if (int(s), int(n)) == (0, 0):
        break
    ndigits = len(n)
    s = int(s)
    cols = (s+2) * ndigits + ndigits - 1
    rows = 2 * s + 3
    screen = [[' '] * cols for _ in range(rows)]
    print_number(screen, s, n)
    print_screen(screen)
    print()
