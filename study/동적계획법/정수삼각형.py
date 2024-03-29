n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [arr[0]]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][0] += arr[i-1][0]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(arr)