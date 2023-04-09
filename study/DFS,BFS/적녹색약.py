import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

normal, unnomarl = 0, 0

do_x = [-1, 1, 0, 0]
do_y = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    current = matrix[x][y]
    for i in range(4):
        nx = x + do_x[i]
        ny = y + do_y[i]

        if (0<=nx<n) and (0<= ny<n) :
            if visited[nx][ny] == False:
                if matrix[nx][ny] == current:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            normal += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] == 'G'

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            unnomarl += 1

print(normal, unnomarl)