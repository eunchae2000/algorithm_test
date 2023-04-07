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
