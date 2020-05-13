# In obedience to the Truth

# uva 718

import itertools

pows = ['1']

while True:
    try:
        n = input()
    except EOFError:
        break
    found = False
    for e in itertools.count():
        print(e, len(pows))
        if len(pows) <= e:
            pows.append(str(2**e))
        else:
            if pows[e].startswith(n) and len(pows[e]) > 2*len(n):
                found = True
                print(e)
                break
    if not found:
        print("no power of 2")



