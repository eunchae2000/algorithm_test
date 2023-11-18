def matrix(x, y):
    i, j = x, y
    row = 1
    col = 1
    
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
            col += 1
        else:
            y -= 1
            break
    
    for a in range(i, x+1):
        for b in range(j, y+1):
            visited[a][b] = True
    
    return [row, col]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    answer = []
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and visited[i][j] == False:
                value = matrix(i, j)
                answer.append(value)
    answer = sorted(answer, key=lambda x:(x[0]*x[1], x[0]))
    
    print(f'#{tc} {len(answer)}', end=" ")
    for j in answer:
        print(*j, end=" ")
    print()