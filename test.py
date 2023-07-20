from collections import deque
n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    result = []
    queue = deque((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and maps[nx][ny] == 1:
                queue.append((nx, ny))
                