# In obedience to the truth

# uva 120

def find_largest_unsorted(stack, start):
    pos_l, l = start, stack[start]
    for i, p in enumerate(stack[start:], start):
        if p > l:
            pos_l, l = i, p
    return pos_l

def reverse(s):
    stack = s.copy()
    ans = []
    first_unsorted = 1
    while first_unsorted < len(stack):
        f = find_largest_unsorted(stack, first_unsorted)
        stack = stack[:f]+list(reversed(stack[f:]))
        stack = stack[:first_unsorted]+list(reversed(stack[first_unsorted:]))
        ans.extend([f, first_unsorted])
        first_unsorted += 1

    return ans


while True:
    try:
        s = [-1] + list(reversed(list(map(int, input().split()))))
    except EOFError:
        break
    ans = reverse(s)
    print(' '.join(map(str, reversed(s[1:]))))
    print(' '.join(map(str, ans)), 0)

