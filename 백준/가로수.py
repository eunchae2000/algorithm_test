import sys
import math

n = int(sys.stdin.readline())
first = int(sys.stdin.readline())
arr = []

for _ in range(n-1):
    num = int(sys.stdin.readline())
    arr.append(num-first)
    first = num

g = arr[0]
for i in range(1, len(arr)):
    g = math.gcd(g, arr[i])

result = 0
for j in arr:
    result += j // g-1

print(result)