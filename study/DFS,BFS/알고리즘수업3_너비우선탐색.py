import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

answer = 1
def bfs(graph, v, visited):
    global answer
    queue = deque([v])
    visited[v] = answer
    
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == 0:
                queue.append(i)
                answer += 1
                visited[i] = answer
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])
    