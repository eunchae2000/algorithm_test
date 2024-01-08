# def solution(n, k):
#     arr = [i for i in range(1, n+1)]
#     answer = 0
    
#     while True:
#         if len(arr) == 1:
#             return arr[0]
#         else:
#             num = arr[0:k]
#             for i in num:
#                 arr.remove(i)
#                 arr.append(i)
#             arr.pop(-1)
            
# print(solution(5, 2))

from collections import deque

def solution(n, k):
    queue = deque(range(1, n+1))
    
    while True:
        if len(queue) == 1:
            return queue[0]
        else:
            for _ in range(k-1):
                queue.append(queue.popleft())
                
                queue.popleft()
print(solution(5, 2))
            