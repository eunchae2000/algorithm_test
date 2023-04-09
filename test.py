from collections import deque
from itertools import combinations
from copy import deepcopy

dx=[1,-1,0,0]
dy=[0,0,1,-1]

N,M=map(int,input().split())
graph=[]
wall=[]
virus=[]
for i in range(N):
    data=list(map(int,input().split()))
    for j in range(M):
        if data[j]==0:
            wall.append([i,j])
        elif data[j]==2:
            virus.append([i,j])

    graph.append(data)

wall_case=combinations(wall,3)

answer=0

for walls in wall_case:

    temp=deepcopy(graph)
    for w in walls:
        wx,wy=w
        temp[wx][wy]=1
    visited=[[False]*M for _ in range(N)]
    q=deque()
    for v in virus:
        vx,vy=v
        q.append([vx,vy])
        visited[vx][vy]=True
    while q:
        x,y=q.popleft()

        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny]==True:
                continue
            if temp[nx][ny]==1:
                continue
            visited[nx][ny]=True
            q.append([nx,ny])
            temp[nx][ny]=2

    safe=0
    for x in range(N):
        safe+=temp[x].count(0)

    answer=max(answer,safe)


print(answer)