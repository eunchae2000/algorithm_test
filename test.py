n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]
visited = [0 for _ in range(n)]
answer = 1

for _ in range(m):
    a, b = map(int, input().split())
    network[a] += [b]
    network[b] += [a]

def dfs(m):
    visited[m] = 1
    for i in network[m]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)