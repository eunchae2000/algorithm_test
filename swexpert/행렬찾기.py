def matrix(x, y):
    i, j = x, y
    row = 1
    column = 1
    
    while True:
        x += 1
        if x<n and data[x][y] != 0 and visited[x][y] == False:
            row += 1
        else:
            x -= 1
            break
    while True:
        y += 1
        if y<n and data[x][y] != 0 and visited[x][y] == False:
            column += 1
        else:
            y -= 1
            break
    
    for k in range(i, x+1):
        for l in range(j, y+1):
            visited[k][l] = True
    
    return [row, column]

for tc in range(1, 11):
    n = int(input())
    answer = []
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and visited[i][j] == False:
                value = matrix(i, j)
                answer.append(value)
    answer = sorted(answer, key=lambda x:(x[0]*x[1], x[0]))