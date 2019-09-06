import sys

def find_broken(n, b, f):
    count_not_broken = n-b

    send = [1] * (n-b) + [0] * b # assume first n-b aren't broken
    not_broken = list(range(n-b+1))
    broken = list(range(n-b+1, n))

    print(''.join(to_send))
    sys.stdout.flush()
    res = input()

    count_of_1 = res.count('1')

    while count_of_1 < count_not_broken:
        if count_of_1 == 0: # reverse guesses
            not_broken, broken = broken, not_broken

        else:
            # find position range of broken
            # build to send accordingly

            print(''.join(send))
            sys.stdout.flush()
            res = input()

    broken = [i for i, j in enumerate(send) if j == '0']
    print(' '.join(broken))
    res = int(input())
    return res



T = int(input())

for _ in range(T):
    n, b, f = [int(s) for s in input().split()]
    ans = find_broken(n, b, f)
    if ans == -1: # wrong guess: exit
        break

