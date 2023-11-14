t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    
    for i in range(n):
        count = 0
        for j in range(n):
            if maps[i][j] == 1:
                count += 1
            if maps[i][j] == 0 or j == n-1:
                if count == k:
                    answer += 1
                count = 0
        
        for j in range(n):
            if maps[j][i] == 1:
                count += 1
            if maps[j][i] == 0 or j == n-1:
                if count == k:
                    answer += 1
                count = 0
    print('#{}'.format(tc), answer)