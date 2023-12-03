from collections import deque

n = int(input())
number = deque(enumerate(map(int, input().split())))
answer = []

while number:
    index, boom = number.popleft()
    answer.append(index+1)
    
    if boom > 0:
        number.rotate(-(boom-1))
    elif boom<0:
        number.rotate(-boom)

print(' '.join(map(str, answer)))