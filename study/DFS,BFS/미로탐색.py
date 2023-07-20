from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]

do_x = [-1, 1, 0, 0]
do_y = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + do_x[i]
            ny = y + do_y[i]

            if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    return maps[n-1][m-1]

print(bfs(0, 0))
