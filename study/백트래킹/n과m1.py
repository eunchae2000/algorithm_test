from itertools import permutations
n, m = map(int, input().split())
arr = list(range(1, n+1))
answer = list(permutations(arr, m))

for i in answer:
    print(*i)