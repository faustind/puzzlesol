if __name__ == '__main__':
    n_test = int(input())

    for _ in range(n_test):
        A, B = tuple(map(int, input().strip().split()))
        n_guess = int(input())

        ans = ''
        for _ in range(n_guess):
            Q = A + (B-A) // 2
            print(Q)
            ans = input()
            if ans == 'CORRECT':
                break
            elif ans == 'TOO_SMALL':
                A = Q
            elif ans == 'TOO_BIG':
                B = Q
            else:
                break
        if ans == 'WRONG_ANSWER':
            break
        else:
            continue
