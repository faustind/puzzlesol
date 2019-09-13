# In Obedience the Truth

# UVa 10050

t = int(input())

for case in range(t):
    ndays = int(input())
    p = int(input())
    hartals = set()
    for _ in range(p):
        h_i = int(input())
        lim = ndays // h_i + 1
        hartals |= {
            d for d in (h_i * i for i in range(1,lim))
            if ( (d % 7) and ((d+1) % 7))
        }
    print(len(hartals))

