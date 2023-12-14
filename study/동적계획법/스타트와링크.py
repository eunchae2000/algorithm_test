import sys
input = sys.stdin.readline

def dfs(n, alist, blist):
    global answer
    if n == N:
        if len(alist) == len(blist):
            a_sum = b_sum = 0
            for i in range(M):
                for j in range(M):
                    a_sum += arr[alist[i]][alist[j]]
                    b_sum += arr[blist[i]][blist[j]]
            answer = min(answer, abs(a_sum-b_sum))
        return
    dfs(n+1, alist+[n], blist)
    dfs(n+1, alist, blist+[n])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N//2
answer = 2147000000
dfs(0, [], [])
print(answer)