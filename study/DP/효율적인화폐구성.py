n, m = map(int, input().split())
array = []
for _ in range(n):
    num = int(input())
    array.append(num)

dp = [10001]*(m+1)
dp[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        # (1-k)원을 만드는 방법이 존재하는 경우
        if dp[j-array[i]] != 10001:
            dp[j] = min(dp[j], dp[j-array[i]]+1)

# m원을 만드는 방법이 없는 경우
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])