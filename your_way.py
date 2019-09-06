import sys

def compute_own_path(n, lpath):
    s = []
    p = []
    for c in lpath:
        if not s or s[-1] == c:
            s.append(c)
        else: # c != s[-1]
            p.extend([c, s.pop()])

    return ''.join(p)

T = int(input())

for case in range(T):
    N = int(input())
    lpath = input()

    ans = compute_own_path(N, lpath)

    print('Case #{}: {}'.format(case+1, ans ))
    sys.stdout.flush()
