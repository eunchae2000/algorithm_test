def dfs(number, row, col):
    if len(number) == 7:
        result.add(number)
        return
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0<=nx<4 and 0<=ny<4:
            dfs(number+maps[nx][ny], nx, ny)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(input())
for tc in range(1, t+1):
    maps = [list(input().split()) for _ in range(4)]
    result = set()
    for x in range(4):
        for y in range(4):
            dfs('', x, y)
            
    print('#{} {}'.format(tc, len(result)))