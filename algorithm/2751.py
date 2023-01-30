n = int(input())
num = []

for i in range(n):
    num.append(int(input()))
numlist = sorted(num)
for i in range(len(num)):
    print(numlist[i])