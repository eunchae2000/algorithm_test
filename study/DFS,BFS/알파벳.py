r, c = map(int, input().split())
aplha = [list(map(lambda x: ord(x)-65, input())) for _ in range(r)]
visited = [False]*26
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c:
            if not visited[aplha[nx][ny]]:
                visited[aplha[nx][ny]] = True
                dfs(nx, ny, count+1)
                visited[aplha[nx][ny]] = False

visited[aplha[0][0]] = True
dfs(0, 0, answer)
print(answer)