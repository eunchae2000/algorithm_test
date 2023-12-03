import sys
from collections import deque

n = int(sys.stdin.readline())
answer = deque()

for i in range(n):
    number = list(map(int, sys.stdin.readline().strip().split()))
    l = len(answer)
    if number[0] == 1:
        answer.appendleft(number[1])
    elif number[0] == 2:
        answer.append(number[1])
    elif number[0] == 3:
        print(answer.popleft() if l else -1)
    elif number[0] == 4:
        print(answer.pop() if l else -1)
    elif number[0] == 5:
        print(len(answer))
    elif number[0] == 6:
        print(0 if l else 1)
    elif number[0] == 7:
        print(answer[0] if l else -1)
    elif number[0] == 8:
        print(answer[-1] if l else -1)