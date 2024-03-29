import math

m, n = map(int, input().split())

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for j in range(m, n+1):
    if prime(j):
        print(j)