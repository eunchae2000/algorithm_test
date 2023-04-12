from collections import deque

def solution(cap, n, deliveries, pickups):
    delive = [[] for _ in range(n+1)]
    answer = []
    for i in range(n):
        delive[i].append(deliveries[i])
        delive[i].append(pickups[i])
    for a, b in delive:
        visited = [False]*n
        visited[b] = True
        result = bfs(n, a, b, visited)
        answer.append(result)
    return min(answer)

def bfs(n, start, delive, visited):
    queue = deque([start, delive])
    visited[start] = True
    count = 1
    while queue:
        v = queue.popleft()
        for i in delive[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count

print(solution(4, 5	, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
