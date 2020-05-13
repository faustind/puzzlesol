# In obedience to the truth

# Uva 10018


def process_int(n):
    ansint = 0
    ansrev = 0
    for i, c in enumerate(reversed(n)):
        ansrev = ansrev*10 + int(c)
        ansint = pow(10,i)*int(c) + ansint
    return ansint, ansrev

if __name__ == '__main__':
    case = int(input())

    for _ in range(case):
        n = input()
        it = 0
        while True:
            np, rn = process_int(n)
            if np == rn:
                ans = np
                break
            else:
                n = str( np + rn )
                it += 1
        print(it, ans)
