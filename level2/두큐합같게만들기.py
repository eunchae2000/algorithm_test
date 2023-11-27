from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1))*4
    sum_queue = sum(queue1)+sum(queue2)
    to1 = sum(queue1)
    to2 = sum(queue2)
    
    if sum_queue % 2 != 0:
        return -1
    
    while True:
        if sum(queue1)>sum(queue2):
            target = queue1.popleft()
            queue2.append(target)
            to1 -= target
            to2 += target
            answer += 1
        elif sum(queue1)<sum(queue2):
            target = queue2.popleft()
            queue1.append(target)
            to1 += target
            to2 -= target
            answer += 1
        else:
            break
        
        if answer == limit:
            answer = -1
            break
    
    return answer
            

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))