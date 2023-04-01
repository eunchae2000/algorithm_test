import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}

for i in range(1, n+1):
    info = sys.stdin.readline().rstrip()
    dict[i] = info
    dict[info] = i

for j in range(m):
    qa = sys.stdin.readline().strip()
    if qa.isdigit():
        print(dict[int(qa)])
    else:
        print(dict[qa])