t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    answer = 0
    start, end = n//2 , n//2
    for i in range(n):
        for j in range(start, end+1):
            answer += farm[i][j]
        if i<n//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print('#{}'.format(tc), answer)
        