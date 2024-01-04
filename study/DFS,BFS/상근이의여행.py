import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tree =[[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    visited = [0]*(n+1)   
     
    def dfs(v, count):
        visited[v] = 1
        for i in tree[v]:
            if visited[i] == 0:
                count = dfs(i, count+1)
        return count
    
    answer = dfs(1, 0)
    print(answer)
    