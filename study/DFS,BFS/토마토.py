from collections import deque
m,n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
count = 0

do_x = [-1, 1, 0, 0]
do_y = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x,  y = queue.popleft()
        for i in range(4):
            nx = x + do_x[i]
            ny = y + do_y[i]
            if 0<= nx < n and 0<= ny < m and tomato[nx][ny]==0:
                queue.append([nx, ny])
                tomato[nx][ny] = tomato[x][y] + 1

bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    count = max(count, max(i))

print(count-1)