p, m = map(int, input().split())
plays = []
for _ in range(p):
    level, player = input().split()
    if not plays:
        plays.append([[int(level), player]])
        continue
    result = False
    for play in plays:
        if len(play) < m and play[0][0]-10 <= int(level) <= play[0][0]+10:
            play.append([int(level), player])
            result = True
            break
    if not result:
        plays.append([[int(level), player]])

for play in plays:
    play.sort(key=lambda x:x[1])

for play in plays:
    if len(play) == m:
        print("Starting!")
    else:
        print("Waiting!")
    for levels, players in play:
        print(levels, players)
