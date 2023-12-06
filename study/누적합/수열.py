import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
answer.append(sum(arr[:m]))
print(answer)

for i in range(n-m):
    answer.append(answer[i]-arr[i]+arr[m+i])

print(max(answer))