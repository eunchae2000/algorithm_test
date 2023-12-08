n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = road[0]*cost[0]
m = cost[0]
dist = 0

for i in range(1, n-1):
    if cost[i] < m:
        res += m*dist
        dist = road[i]
        m = cost[i]
    else:
        dist += road[i]
    
    if i == n-2:
        res += m*dist
print(res)