import sys

# input 대신 sys.stdin.readline을 사용하면 실행 시간을 줄일 수 있음
n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

num.sort(key=lambda x:(x[1], x[0]))

for i in num:
    print(i[0], i[1])