# In Obedience to the Truth

# uva 10067

# TLE
# I don't get it sniff... Hahaha sniff...

import collections

# bfs
def bfs(start: int):
    """bfs.
    TODO: initialize discovered[], processed[] and parent[]
    """
    q = collections.deque()

    q.append(start)
    discovered[nv(start)] = 0

    while q:
        v = q.pop()
        if nv(v) not in forbidden:
            for ne in adj(v):
                y = ne
                if (not discovered[nv(y)]) and (nv(y) not in forbidden):
                    q.appendleft(y)
                    discovered[nv(y)] = discovered[nv(v)] + 1
                if y == end:
                    return

def left(i: int):
    if i == 0:
        return 9
    else:
        return i - 1

def right(i: int):
    if i == 9:
        return 0
    else:
        return i + 1

def adj(n: list):
    a,b,c,d = n
    return [[left(a), b, c, d],
            [right(a), b, c, d],
            [a, left(b), c, d],
            [a, right(b), c, d],
            [a, b, left(c), d],
            [a, b, right(c), d],
            [a, b, c, left(d)],
            [a, b, c, right(d)]]

def nv(n):
    return int(''.join(map(str, n)))


if __name__ == "__main__":
    c = int(input())

    while c:
        c -= 1

        input()

        start = list(map(int, input().split()))
        end = list(map(int, input().split()))


        fn = int(input())

        discovered = [False] * 10000

        forbidden = []
        for _ in range(fn):
            forbidden.append ( int(''.join(input().split())) )

        if (nv(end) in forbidden) or (nv(start) in forbidden):
            print('-1')

        bfs(start)

        print(discovered[nv(end)] or -1)
