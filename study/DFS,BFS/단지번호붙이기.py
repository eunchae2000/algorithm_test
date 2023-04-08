n = int(input())
apart = [list(map(int, input())) for _ in range(n)]
do_x = [-1, 1, 0, 0]
do_y = [0, 0, -1, 1]
answer = 0
visited = []
result = 0

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>= n:
        return False
    if apart[x][y] == 1:
        global answer
        answer += 1
        apart[x][y] = 0
        for i in range(4):
            nx = x + do_x[i]
            ny = y + do_y[i]
            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            visited.append(answer)
            result += 1
            answer = 0

visited.sort()
print(result)
for i in visited:
    print(i)