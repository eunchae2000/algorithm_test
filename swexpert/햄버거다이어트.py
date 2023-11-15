t = int(input())
for tc in range(1, t+1):
    n, l = map(int, input().split())
    score = []
    kcal = []
    def dfs(i, taste, kcalo):
        global answer
        if kcalo > l:
            return
        if taste > answer:
            answer = taste
        if i == n:
            return
        dfs(i+1, taste+score[i], kcalo+kcal[i])
        dfs(i+1, taste, kcalo)
    for _ in range(n):
        s, k = map(int, input().split())
        score.append(s)
        kcal.append(k)
    answer = 0
    dfs(0, 0, 0)
    print('#{}'.format(tc), answer)