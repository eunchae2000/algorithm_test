from itertools import product

n, m = map(int, input().split())
arr = list(range(1, n+1))
result = list(product(arr, repeat=m))
for i in result:
    print(*i)