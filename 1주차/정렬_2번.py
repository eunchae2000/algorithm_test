n = int(input())

num = [input() for _ in range(n)]
num.sort()

for i in num:
    print(i)