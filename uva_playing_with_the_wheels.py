# In Obedience to the Truth

# uva 10067

import collections


def bfs(start):
    q = collections.deque()

    q.append(start)
    discovered[start] = 0

    while q:
        v = q.pop()
        if v == end:
            return
        for y in adj(v):
            if discovered[y]:
                continue
            discovered[y] = discovered[v] + 1
            if y not in forbidden:
                q.appendleft(y)


def adj(n):
    a,b,c,d = n
    def left(i):
        if i == 0:
            return 9
        else:
            return i - 1

    def right(i):
        if i == 9:
            return 0
        else:
            return i + 1

    return [(left(a), b, c, d),
            (right(a), b, c, d),
            (a, left(b), c, d),
            (a, right(b), c, d),
            (a, b, left(c), d),
            (a, b, right(c), d),
            (a, b, c, left(d)),
            (a, b, c, right(d))]

if __name__ == "__main__":
    c = int(input())

    while c:
        c -= 1

        try:
            input()
        except Exception:
            break

        start = tuple(int(c) for c in input().split())
        end = tuple(int(c) for c in input().split())

        fn = int(input())

        discovered = collections.defaultdict(lambda: None)

        forbidden = set()
        for _ in range(fn):
            forbidden.add ( tuple(int(c) for c in input().split()) )

        if end == start:
            print(0)
            continue

        if end in forbidden:
            print(-1)
            continue


        bfs(start)

        print(discovered[end] if discovered[end] is not None else -1)
