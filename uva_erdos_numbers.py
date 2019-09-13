# In Obedience to the Truth

# UVa 10044

import collections

def update_coauthors(author):
    for name in coauthors[author]:
        if numbers[name] > numbers[author]+1:
            numbers[name] = numbers[author]+1
            update_coauthors(name)


scenarios = int(input())

for scen in range(scenarios):
    numbers = collections.defaultdict(lambda:float('inf'))
    coauthors = collections.defaultdict(set)

    numbers['Erdos, P.'] =  0

    p, n = map(int, input().split())

    for _ in range(p):
        authors, paper = input().split(': ')
        ns = authors.split(', ')
        authors = {ns[i]+', '+ns[j] for i, j in zip(range(0, len(ns)-1, 2),\
                                                    range(1, len(ns), 2))}

        #print('paper: ', paper, 'authors: ', authors)
        minnum, minauthor = float('inf'), None
        for author in authors:
            coauthors[author] |= (authors - {author})
            if numbers[author] < minnum:
                minnum, minauthor = numbers[author], author
        #print('minnum', minnum, 'minauthor', minauthor)

        for author in authors:
            if author is not minauthor:
                if numbers[author] > minnum+1:
                    numbers[author] = minnum+1
                    update_coauthors(author)
        #print(numbers)

    print('Scenario {}'.format(scen+1))
    for _ in range(n):
        name = input().strip()
        if numbers[name] == float('inf'):
            print(name, 'infinity')
        else:
            print(name, numbers[name])


