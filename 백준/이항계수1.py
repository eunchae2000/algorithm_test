n, k = map(int, input().split())
num1 = 1
num2 = 1
num3 = 1
answer = 0

for i in range(1, n+1):
    num1 *= i

for i in range(1, (n-k)+1):
    num2 *= i
    
for i in range(1, k+1):
    num3 *= i

print(num1//(num2*num3))