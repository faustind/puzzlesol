# In obedience to the truth

# UVa 10052

from collections import Counter

while True:
    try:
        a = input()
        b = input()
    except EOFError:
        break
    a = Counter(a)
    b = Counter(b)

    common = a & b

    print(''.join(sorted(common.elements())))
