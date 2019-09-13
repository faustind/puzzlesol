# In Obedience to the Truth

# UVa 10258


import collections

PENALTY = 20

nc = int(input())
input()

for case in range(nc):

    contestants  = [None] * 101
    penalty = collections.defaultdict(int)
    solved = collections.defaultdict(int)

    solved_by_contestant = collections.defaultdict(set)

    while True:
        try:
            s = input()
        except EOFError:
            break
        if s != '':
            c, p, t, l = s.split()
            c, p, t = int(c), int(p), int(t)

            # make sure contestants with submitions appear on the board
            penalty[c] += 0
            solved[c] += 0

            if contestants[c] is None:
                contestants[c] = dict()
            if l.upper() == 'I' and p not in solved_by_contestant[c]:
                # increase penalty of problem p for contestant c
                contestants[c][p] = contestants[c].get(p, 0) + 1
            elif l.upper() == 'C' and p not in solved_by_contestant[c]:
                # update total penalty for contestant c for solved problem
                solved_by_contestant[c].add(p)
                penalty[c] += contestants[c].get(p, 0) * PENALTY + t
                solved[c] += 1
        else:
            break

    board = sorted(list((-solved[k], penalty[k], k) for k in penalty))
    for score in board:
        print(score[2], -score[0], score[1])

    if case == nc-1:
        break
    print()
