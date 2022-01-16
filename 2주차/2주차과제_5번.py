from collections import deque

N = int(input())
num = deque()

for i in range(N):
    d = input().split()
    if d[0] == 'push_front':
        num.appendleft(d[1])
    elif d[0] == 'push_back':
        num.append(d[1])
    elif d[0] == 'pop_front':
        if len(num) == 0:
            print(-1)
        else:
            print(num.popleft())
    elif d[0] == 'pop_back':
        if len(num) == 0:
            print(-1)
        else:
            print(num.pop())
    elif d[0] == 'size':
        print(len(num))
    elif d[0] == 'empty':
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif d[0] == 'front':
        if len(num) == 0:
            print(-1)
        else:
            print(num[0])
    elif d[0] == 'back':
        if len(num) == 0:
            print(-1)
        else:
            print(num[-1])