# In obedience to the truth

# UVa 10041

import collections

k = int(input())

for _ in range(k):
    d = list(map(int, input().split()))

    pd = sorted(d[1:])
    mid = pd[len(pd)//2]

    min = sum(abs(mid-p) for p in pd)

    print(min)
