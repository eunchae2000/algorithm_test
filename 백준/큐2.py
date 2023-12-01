import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    string = sys.stdin.readline().rstrip()
    
    if len(string) > 5:
        queue.append(int(string[5:]))
    if string == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    if string == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    if string == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if string == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    if string == 'size':
        print(len(queue))