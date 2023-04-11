visited = []
answer = 0

def solution(k,dungeons):
    global visited
    visited = [False]*len(dungeons)
    dfs(k, dungeons, 0)
    return answer

def dfs(k, dungeons, count):
    global answer
    if count > answer:
        answer = count
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k-dungeons[i][1], dungeons, count+1)
            visited[i] = False

print(solution(80,[[80,20],[50,40],[30,10]]))