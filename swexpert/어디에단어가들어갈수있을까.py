t = int(input())
for m in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or j == n-1:
                if count == k:
                    answer += 1
                if arr[i][j] == 0:
                    count = 0
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j][i] == 1:
                count += 1
            if arr[j][i] == 0 or j == n-1:
                if count == k:
                    answer += 1
                if arr[j][i] == 0:
                    count = 0
    print("#{} {}".format(m, answer))