t = int(input())
answer = 0
for _ in range(t):
    m, n, k = map(int, input().split())
    baechu = [[0]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        baechu[a][b] = 1
    for i in range(m):
        for j in range(n):
            if baechu[i][j] == 1:
                dfs(i, j)
                answer += 1

print(answer)

def dfs(x, y):
    do_x = [-1, 1, 0, 0]
    do_y = [0, 0, -1, 1]

    for i in range(4):
        nx = x + do_x[i]
        ny = y + do_y[i]
        if (0<=nx<m) and (0<=ny<n):
            if baechu[nx][ny] == 1:
                baechu[nx][ny] = -1
                dfs(nx, ny)



