from collections import deque

def solution(maps):

    dox = [-1, 1, 0, 0]
    doy = [0, 0, -1, 1]

    row, col = len(maps), len(maps[0])

    graph = [[-1 for _ in range(col)] for _ in range(row)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dox[i]
            ny = y + doy[i]

            if 0 <= nx < row and 0<= ny < col and maps[nx][ny] == 1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])
    return graph[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))