t = int(input())
for tc in range(1, t+1):
    n = int(input())
    answer =[]
    count = 0
    for i in range(0, n):
        result = []
        for j in range(0, i+1):
            if j == 0 or j==i:
                result.append(1)
                print(result)
            if j != 0 and j != i:
                result.append(count)
                print(result)
        answer.append(result)
        count += 1
    print(f'#{tc}')
    for x in range(n):
        for y in range(len(answer[x])):
            print(answer[x][y], end=" ")
        print()