import sys

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        n = int(input())
        s = list(map(int, input().rstrip()))

        mid = (n+1) // 2
        max_so_far = sum(s[:mid])
        old = max_so_far
        for o, i in enumerate(range(mid, len(s))):
            max_so_far = max(max_so_far, old + s[i] - s[o])
            old = old + s[i] - s[o]

        print('Case #' + str(case+1) +': '+ str(max_so_far) )
        sys.stdout.flush()
