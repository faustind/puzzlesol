# In obedience to the truth

# Uva 10035

import itertools

while True:
    try:
        a, b = input().split()
        if a == "0" and b == "0":
            break
    except EOFError:
        break

    a, b = map(reversed, (a,b))

    count, carry = 0, 0
    for ai, bi in itertools.zip_longest(a,b, fillvalue='0'):
        if int(ai) + int(bi) + carry > 9:
            carry = 1
            count += 1
        else:
            carry = 0

    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print("{} carry operations.".format(count))


