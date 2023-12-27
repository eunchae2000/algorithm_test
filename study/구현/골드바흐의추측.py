import sys

def prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    a = num//2
    b = num//2
    while True:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1