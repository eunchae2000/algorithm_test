from collections import deque
import copy
import sys

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0
n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def wall_con(wall):
    if wall == 3:
        virus()
        return 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall_con (wall+1)
                lab[i][j] = 0

def virus():
    queue = deque()
    maps = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if (0<=nx<n) and (0<=ny<m) and (maps[nx][ny] == 0):
                maps[nx][ny] = 2
                queue.append((nx, ny))
    
    global answer
    count = 0
    for i in maps:  
        count += i.count(0)
    answer = max(answer, count)


wall_con(0)
print(answer)