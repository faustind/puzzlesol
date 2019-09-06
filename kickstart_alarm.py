import sys
import collections

Input = collections.namedtuple('Input',
                               ('N', 'K', 'x1', 'y1', 'C', 'D', 'E1', 'E2', 'F'))

def power(x, y):
    ans, power = 1, y
    if y < 0:
        power, x = -power, 1 / x
    while power:
        if power & 1:
            ans *= x
        x, power = x ** 2, power >> 1
    return ans


def compute_power_sum(arr, k):
    result = 0
    GP_sum = k
    mod = 1_000_000_007
    for x, A_x in enumerate(arr[1:], 1):
        if x != 1:
            GP_sum = GP_sum + (power(x, k+1)-1) * power(x-1, mod-2)
            GP_sum %= mod

        result = result + GP_sum * A_x
        result %= mod
    return result


if __name__ == '__main__':
    T = int(input())

    for case in range(1, T+1):
        params = Input(*map(int, input().rstrip().split()))

        A = [0] * (params.N+1)
        A[1] = (params.x1 + params.y1) % params.F
        old_xi, old_yi = params.x1, params.y1
        for i in range(2, params.N+1):
            xi = (params.C * old_xi + params.D * old_yi + params.E1)  % params.F
            yi = (params.D * old_xi + params.C * old_yi + params.E2)  % params.F
            old_xi, old_yi = xi, yi
            A[i] = (xi + yi) % params.F

        ans = compute_power_sum(A, params.K)
        print('Case #'+str(case)+': '+str(int(ans)))

