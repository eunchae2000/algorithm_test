N = int(input())
num = (list(map(int, input().split())))
result = []
answer = [-1 for _ in range(N)]

for i in range(len(num)):
    while len(result) != 0 and num[result[-1]] < num[i]:
        answer[result.pop()] = num[i]
    result.append(i)

print(*answer)

