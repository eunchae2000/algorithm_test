import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

answer = 1
def dfs(graph, v, visited):
    global answer
    visited[v] = answer
    graph[v].sort(reverse=True)
    
    for i in graph[v]:
        if visited[i] == 0:
            answer += 1
            dfs(graph, i, visited)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, r, visited)
for i in range(1, n+1):
    print(visited[i])