# In obedience to the truth

# UVa 10010

directions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

def lookup(word, pos, d, grid):
    #print('lookup({}, ({}, {}), {}, grid)'.format(word, pos[0], pos[1], d))
    if len(word) == 0:
        return True
    if not ( 1 <= pos[0] <= M and 1 <= pos[1] <= N):
        return False
    if word[0] == grid[ pos[0] ][ pos[1] ]:
        pos = (pos[0]+d[0], pos[1]+d[1])
        return lookup(word[1:], pos, d, grid)
    return False

def search(word, grid):
    found = False
    m, line = 1, grid[1]
    for m, line in enumerate(grid[1:], 1):
#        print('line {}, {}'.format(m, line))
        i = 0
        for n, char in enumerate(line[1:], 1):
            if char == word[0]: # the first letter of the word
                for d in directions:
                    #print('lookup({}, ({}, {}), {}, grid)'.format(word, m, n, d))
                    found = lookup(word, (m, n), d, grid)
                    if found:
                        break
            if found:
                return (m, n)




t = int(input())
input()

for c in range(t):
    M, N = map(int, input().split())

    grid = [[]]
    for _ in range(M):
        grid.append([None]+list(input().lower()))
    #print(grid)

    k = int(input())
    for _ in range(k):
        word = input().lower()
        ans = search(word, grid)
        print('{} {}'.format(ans[0], ans[1]))

    if c != t-1:
        print()
        input()
