import sys
from collections import deque

n = int(sys.stdin.readline())
def solution(n):
    queue = deque(range(1, n+1))
    
    while len(queue) >1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

print(solution(n))