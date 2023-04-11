from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = n
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for start, not_visited in wires:
        visited = [False]*(n+1)
        visited[not_visited] = True
        result = bfs(start, visited, graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result-(n-result))
    return answer

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

