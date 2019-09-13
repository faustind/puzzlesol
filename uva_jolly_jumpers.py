# In Obedience to the Truth

# UVa 10038

while True:
    try:
        v = list(map(int, input().split()))
    except EOFError:
        break
    if not v:
        break
    j = [False] * len(v)
    j[0], j[-1] = True, True
    if len(v)-1 != v[0]:
        print('Not jolly')
    ans = False
    for i in range(2, len(v)):
        test = abs(v[i] - v[i-1])
        if (1 <= test <= v[0]-1) and not j[test]:
            j[test] = True
        else:
            #print('ans, test, i, j', test, i, j)
            print('Not jolly')
            ans = True
            break
    if not ans:
        #print('nans', j)
        if all(j):
            print('Jolly')
        else:
            print('Not Jolly')




