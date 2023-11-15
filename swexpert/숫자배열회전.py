t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    
    maps_90 = [[0 for _ in range(n)] for _ in range(n)]
    maps_180 = [[0 for _ in range(n)] for _ in range(n)]
    maps_270 = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            maps_90[i][j] = maps[n-1-j][i]
    
    for i in range(n):
        for j in range(n):
            maps_180[i][j] = maps_90[n-1-j][i]
            
    for i in range(n):
        for j in range(n):
            maps_270[i][j] = maps_180[n-1-j][i]
    
    print(f'#{tc}')
    for i in range(n):
        for a in range(n):
            print(maps_90[i][a], end="")
        print(end=" ")
        for b in range(n):
            print(maps_180[i][b], end="")
        print(end=" ")
        for c in range(n):
            print(maps_270[i][c], end="")
        print()