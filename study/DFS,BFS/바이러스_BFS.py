from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
v = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
def bfs(v):
    queue = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
    return sum(visited)-1

print(bfs(v))