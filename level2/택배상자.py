def solution(order):
    belt = [i for i in range(1, len(order)+1)]
    stack = []
    current_index = 0
    count = 0
    
    for box in belt:
        while stack and stack[-1] == order[current_index]:
            stack.pop()
            count += 1
            current_index += 1
        
        if box == order[current_index]:
            count += 1
            current_index += 1
        else:
            stack.append(box)
    
    while stack:
        if stack[-1] == order[current_index]:
            count += 1
            current_index += 1
            stack.pop()
        else:
            break
    return count

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
    
    