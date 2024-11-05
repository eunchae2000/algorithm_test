from collections import deque

def bfs(maps, i, j, n, m, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    days = int(maps[i][j])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                days += int(maps[nx][ny])
                queue.append((nx, ny))
    return days

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = []
    visited = [[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(maps, i, j, n, m, visited))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]