total = int(input())
num = int(input())
real_total = 0

for i in range(num):
    a, b = map(int, input().split())
    real_total += a*b

if(real_total == total):
    print("Yes")
else:
    print("No")
