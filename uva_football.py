# In obedience to the truth

# uva 10191

import collections

def parse_game(game):
    home, away = game.split('@')
    home_name, home_goal = home.split('#')
    away_goal, away_name = away.split('#')
    home_goal, away_goal = int(home_goal), int(away_goal)
    return (home_name, home_goal, away_name, away_goal)


n = int(input())
for k in range(n):
    teams = collections.defaultdict(dict)
    tname = input()
    t = int(input())
    for _ in range(t):
        ti = input()
        teams[ti]['name'] = ti
        teams[ti]['p'] = 0 # points
        teams[ti]['w'] = 0 # most win
        teams[ti]['gd'] = 0 # goal diff
        teams[ti]['gs'] = 0 # goal scored
        teams[ti]['ga'] = 0 # goal against
        teams[ti]['gp'] = 0 # game played
        teams[ti]['tie'] = 0
        teams[ti]['losses'] = 0

    g = int(input())
    for _ in range(g):
        game = input()
        h, hg, a, ag = parse_game(game)

        teams[a]['gd'] += (ag-hg)
        teams[a]['gs'] += ag
        teams[a]['ga'] += hg

        teams[h]['gd'] += (hg-ag)
        teams[h]['gs'] += hg
        teams[h]['ga'] += ag


        teams[h]['gp'] += 1
        teams[a]['gp'] += 1

        if hg > ag:
            teams[h]['p'] += 3
            teams[h]['w'] += 1
            teams[a]['losses'] += 1
        elif hg < ag:
            teams[a]['p'] += 3
            teams[a]['w'] += 1
            teams[h]['losses'] += 1
        else:
            teams[a]['p'] += 1
            teams[a]['tie'] += 1
            teams[h]['p'] += 1
            teams[h]['tie'] += 1

    rankedt = sorted(teams.values(),
                    key=lambda t: (-t['p'],-t['w'],-t['gd'],-t['gs'],t['gp'],t['name'].lower())
                    )
    print(tname)
    for i, t in enumerate(rankedt,1):
        print('{}) {} {}p, {}g ({}-{}-{}), {}gd ({}-{})'.format(
            i, t['name'], t['p'], t['gp'], t['w'], t['tie'], t['losses'], t['gd'], t['gs'], t['ga']
            ))

    if k < n-1:
        print()

