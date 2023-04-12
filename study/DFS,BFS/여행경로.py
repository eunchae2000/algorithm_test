from collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    queue.append(("ICN", ["ICN"], []))

    while queue:
        start, path, used = queue.popleft()
        if len(used) == len(tickets):
            answer.append(path)
        for index, locate in enumerate(tickets):
            if locate[0] == start and index not in used:
                queue.append(([locate[1], path+[locate[1]], used+[index]]))

    answer.sort()
    return answer[0]

# def solution(tickets):
#     answer = []
    
#     visited = [False]*len(tickets)
    
#     def dfs(airport, path):
#         if len(path) == len(tickets)+1:
#             answer.append(path)
#             return
        
#         for idx, ticket in enumerate(tickets):
#             if airport == ticket[0] and visited[idx] == False:
#                 visited[idx] = True
#                 dfs(ticket[1], path+[ticket[1]])
#                 visited[idx] = False
        
        
#     dfs("ICN", ["ICN"])
    
#     answer.sort()

#     return answer[0]