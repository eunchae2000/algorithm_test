N = int(input())
stack = []
result = 0

for i in range(N):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

for j in stack:
    result += j

print(result)