import sys

n = int(sys.stdin.readline())
info = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

info.sort(key=lambda x:int(x[0]))

for i in info:
    for j in i:
        print(j, end=" ")
    print()
