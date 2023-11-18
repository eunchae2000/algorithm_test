t = int(input())
for tc in range(1, t+1):
    n, q = map(int, input().split())
    number = [0]*n
    count = 1
    for i in range(q):
        a, b = map(int, input().split())
        for j in range(a-1, b):
            number[j] = count
        count += 1
    print(f'#{tc}', end=" ")
    print(*number)
        