def solution(n, computers):
    answer = 0
    dfs_visit = [False for i in range(n)]
    for com in range(n):
        if dfs_visit[com] == False:
            dfs(n, computers, com, dfs_visit)
            answer += 1
    return answer

def dfs(n, computers, com, dfs_visit):
    dfs_visit[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if dfs_visit[connect] == False:
                dfs(n, computers, connect, dfs_visit)
