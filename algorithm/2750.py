n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num = sorted(num)

for i in range(len(num)):
    print(num[i])