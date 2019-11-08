# In obedience to the truth

# UVa 10132

import collections

n = int(input())
input()

for c in range(n):
    fs = collections.defaultdict(list)
    n, tl = 0, 0 # number of fragments, cumulated length
    min_key, max_key = float('Inf'), float('-Inf') # minmax length of fragments
    while True:
        try:
            f = input()
            if f:
                min_key, max_key = min(min_key, len(f)), max(max_key, len(f))
                fs[len(f)].append(f)
                n, tl = n+1, tl+len(f)
            else:
                break
        except Exception:
            break

    len_ans = tl // ( n // 2 ) # length of recovered filel
    kl = sorted(fs.keys())

    candidates = collections.Counter()
    li, hi = 0, len(kl)-1
    while li <= hi:
        l, h = kl[li], kl[hi]
        if not l+h == len_ans:
            continue

        for fl in set(fs[l]):
            if len(set(fs[h])-{fl}) == 0:
                candidates.update([fl*(len_ans//l)])
            else:
                for fh in set(fs[h])-{fl}:
                    candidates.update([fl+fh, fh+fl])

        li, hi = li+1, hi-1

    if c > 0:
        print()
    print(candidates.most_common(1)[0][0])
    if c == n-1:
        break

