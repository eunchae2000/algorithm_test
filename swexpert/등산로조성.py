dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, path, isConst):
    global answer
    if answer < path:
        answer = path
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if visited[nx][ny] == 1:
            continue
        if arr[x][y] > arr[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, path+1, isConst)
            visited[nx][ny] = 0


t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    for a in range(n):
        for b in range(n):
            if max_num < arr[a][b]:
                max_num = arr[a][b]
    answer = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] == max_num:
                visited = [[0]*n for _ in range(n)]
                visited[a][b] = 1
                dfs(a, b, 1, False)
    print("#{} {}".format(i, answer))