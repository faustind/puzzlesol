"""Build the masked mine field given the position of the mines."""
def inrange(i, j, f):
    return ((0 <= i < len(f))
            and (0 <= j < len(f[0]))
            and (f[i][j] != '*'))

def update_for_mine(f, i, j):
    if inrange(i-1, j, f):
        # just above
        f[i-1][j] += 1
    if inrange(i+1, j, f):
        # just below
        f[i+1][j] += 1
    if inrange(i, j-1, f):
        # just on the left
        f[i][j-1] += 1
    if inrange(i, j+1, f):
        # just on the right
        f[i][j+1] += 1
    if inrange(i-1, j-1, f):
        # top left
        f[i-1][j-1] += 1
    if inrange(i-1, j+1, f):
        # top left
        f[i-1][j+1] += 1
    if inrange(i+1, j+1, f):
        # bottom right
        f[i+1][j+1] += 1
    if inrange(i+1, j-1, f):
        # bottom left
        f[i+1][j-1] += 1

case = 1
while True:
    l, c = map(int, input().split())
    if (l, c) == (0, 0):
        break

    m = [[0] * c  for _ in range(l)]

    for i in range(l):
        for j, c in enumerate(input()):
            if c  == '*':
                m[i][j] = '*'
                update_for_mine(m, i, j)
    if case > 1:
        print()
    print('Field #{}:'.format(case))
    for l in m:
        print(''.join(str(i) for i in l))
    case += 1

