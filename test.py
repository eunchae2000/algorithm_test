import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
        
t = int(input())
for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                dfs(a, b)
                count += 1
    print(count)
