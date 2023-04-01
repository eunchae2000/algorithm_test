import sys

n = int(sys.stdin.readline())
result = {}
for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())
    if status == 'enter':
        result[name] = 1
    elif status == 'leave':
        del result[name]

result = sorted(result.keys(), reverse=True)

for i in result:
    print(i)
