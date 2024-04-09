from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    cnt = 0
    
    while board[x+dx][y+dy] != '#' and board[x][y] != '0':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque([(rx, ry, bx, by, 1)])
    visited[rx][ry][bx][by] = True
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth>10:
            break
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return depth
            
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
                    
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
                
    return -1

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by))