t = int(input())
for i in range(1, t+1):
    n = int(input())
    dx = []
    dy = []
    for num in range(n, 0, -1):
        for _ in range(num):
            dx.append(0)
            dy.append(1-(2)*((n-num)%2))
        for _ in range(num-1):
            dx.append(1-(2)*((n-num)%2))
            dy.append(0)
    arr = [[0]*n for _ in range(n)]
    x = y = 0
    for num in range(1, n*n+1):
        if num == 1:
            arr[x][y] = 1
        else:
            x += dx[num-1]
            y += dy[num-1]
            arr[x][y] = num
    print("#{}".format(i))
    for answer in arr:
        print(*answer)