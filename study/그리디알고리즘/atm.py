n = int(input())
num = list(map(int, input().split()))
num.sort()
answer = [num[0]]

for i in range(1, len(num)):
    result = answer[-1]+num[i]
    answer.append(result)

print(sum(answer))