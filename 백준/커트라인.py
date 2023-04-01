import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)

print(a[k-1])
