for tc in range(1, 11):
    num = int(input())
    maps = [[] for _ in range(16)]
    start = (0, 0)
    check = False
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(16):
        now = list(map(int, list(input())))
        if 2 in now:
            tmp = now.index(2)
            start = (i, tmp)
        maps[i] = now
        
    def dfs(x, y):
        global check
        if x<0 or y<0 or x>=16 or y>=16 or maps[x][y] == 1 or check:
            return
        
        if maps[x][y] == 3:
            check = True
            return
        
        if maps[x][y] == 0 or 2:
            maps[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
    
    dfs(start[0], start[1])
        
    print(f'#{num} {"1" if check else "0"}')