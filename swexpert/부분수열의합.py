# from itertools import combinations, permutations
# t = int(input())
# for tc in range(1, t+1):
#     n, k = map(int, input().split())
#     num = list(map(int, input().split()))
#     answer = 0
#     for i in range(1, n+1):
#         com = combinations(num, i)
#         for c in com:
#             if sum(c) == k:
#                 answer+=1
    
#     print(f'#{tc}', end=" ")
#     print(answer)

from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    number = list(map(int, input().split()))
    answer = 0
    que = deque()
    
    que.append((1, number[0]))
    que.append((1, 0))
    while que:
        q = que.popleft()
        if q[0] == n:
            if q[1] == k:
                answer += 1
        else:
            que.append((q[0]+1, q[1]+number[q[0]]))
            que.append((q[0]+1, q[1]))
    print(f'#{tc} {answer}')
        