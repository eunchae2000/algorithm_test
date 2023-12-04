from itertools import combinations
n, m = map(int, input().split())
arr = list(range(1, n+1))
answer = list(combinations(arr, m))

for i in answer:
    print(*i)