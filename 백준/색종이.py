arr = [[0 for _ in range(101)] for _ in range(101)]
num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            arr[j][k] = 1

result = 0

for a in arr:
    result += a.count(1)

print(result)