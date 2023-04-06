from collections import deque
n, m, v = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_visit = [False]*(n+1)
bfs_visit = [False]*(n+1)

def dfs(v):
    dfs_visit[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not dfs_visit[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    bfs_visit[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not bfs_visit[i] and graph[v][i]:
                queue.append(i)
                bfs_visit[i] = True
dfs(v)
print()
bfs(v)