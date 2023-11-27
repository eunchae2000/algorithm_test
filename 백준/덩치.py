n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = []
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i][0] <  arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    answer.append(count+1)


for num in answer:
    print(num, end=" ")