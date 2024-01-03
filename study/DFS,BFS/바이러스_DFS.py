import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return sum(visited)-1

print(dfs(1))