import sys

K = int(sys.stdin.readline())

stack = []
result = 0
for i in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

for i in stack:
    result += i

print(result)