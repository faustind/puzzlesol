# In Obedience to the truth

# UVa 10137

# Note: WA

def money_to_exchange(e):
    """Compute minimal amount of money to be exchange to equalized each entry of e within one cent"""

    avg = sum(e) / len(e)

    pos, neg = 0, 0
    for val in e:
        diff = (int((val - avg)))
        if diff > 0:
            pos += diff
        elif diff < 0:
            neg += diff

    neg = -neg if neg < 0.0 else neg

    return max(neg, pos) / 100.0

while True:
    std = int(input())
    if std == 0:
        break
    e = []
    for _ in range(std):
        e.append(int( float(input()) * 100))

    ans = money_to_exchange(e)
    print('${:.2f}'.format(ans))
