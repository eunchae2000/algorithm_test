import math
import sys

answer = 0

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

prime_list = []
for j in range(2, 123456*2+1):
    if prime(j):
        prime_list.append(j)

while True:
    n = int(sys.stdin.readline())
    answer = 0
    if n == 0:
        break
    for k in prime_list:
        if k>2*n:
            break
        elif n<k<=2*n:
            answer+=1
    print(answer)