from collections import deque

def is_valid(nx, ny, n, m, maps):
    return 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X'

def queue_append(nx, ny, k, time, visited, queue):
    if not visited[nx][ny][k]:
        visited[nx][ny][k] = True
        queue.append((nx, ny, k, time+1))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    end_x, end_y = -1, -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                queue.append((i, j, 0, 0))
                visited[i][j][0] = True
            if maps[i][j] == 'E':
                end_x, end_y = i, j
    
    while queue:
        x, y, k, time = queue.popleft()
        
        if x == end_x and y == end_y:
            return time
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not is_valid(nx, ny, n, m, maps):
                continue
            
            if maps[nx][ny] == 'L':
                queue_append(nx, ny, 1, time, visited, queue)
            else:
                queue_append(nx, ny, k, time, visited, queue)
    return -1
