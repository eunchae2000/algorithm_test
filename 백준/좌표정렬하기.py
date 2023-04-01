n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))

num.sort()

for i in num:
    for j in i:
        print(j, end=" ")
    print()