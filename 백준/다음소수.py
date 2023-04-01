import math

n = int(input())
result = 0

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for _ in range(n):
    a = int(input())
    while True:
        if prime(a):
            print(a)
            break
        else:
            a += 1