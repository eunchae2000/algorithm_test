n = int(input())
num = list(map(int, str(n)))
num.sort()

for i in num:
    print(i, end="")
    