import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    do_x = [-1, 1, 0, 0]
    do_y = [0, 0, -1, 1]

    for i in range(4):
        nx = x + do_x[i]
        ny = y + do_y[i]
        if 0<=nx<m and 0<=ny<n:
            if baechu[nx][ny] == 1:
                baechu[nx][ny] = -1
                dfs(nx, ny)

t = int(input())

for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    baechu = [[0]*n for _ in range(m)]
    for j in range(k):
        a, b = map(int, input().split())
        baechu[a][b] = 1
    for a in range(m):
        for b in range(n):
            if baechu[a][b] == 1:
                dfs(a, b)
                count += 1
    print(count)