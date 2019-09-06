import sys

def solution(n):
    a, b, p = 0, 0, 0
    while n:
        i = (n % 10)
        if i == 4:
            a += 1 * 10**p
            b += 3 * 10**p
        else:
            a += i * 10 ** p
        n, p = n//10, p+1

    return a, b


T = int(input())
for case in range(T):
    n = int(input())
    a, b = solution(n)
    print('Case #{}: {} {}'.format(case+1, a, b))
    sys.stdout.flush()
