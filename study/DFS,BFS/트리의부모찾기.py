import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v):
    for i in arr[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)
dfs(1)

for i in range(2, n+1):
    print(visited[i])