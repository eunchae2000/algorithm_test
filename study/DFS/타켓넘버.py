# BFS
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0], 0]]
    n = len(numbers)

    while queue:
        value, index = queue.pop()
        index += 1
        if index < n:
            queue.append([value + numbers[index], index])
            queue.append([value - numbers[index], index])
        else:
            if value == target:
                answer += 1
    return answer

# DFS
# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(index, value):
#         if index == n:
#             if value == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(index + 1, value + numbers[index])
#             dfs(index + 1, value - numbers[index])
#     dfs(0, 0)
#     return answer

