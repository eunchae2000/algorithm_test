t = int(input())
for tc in range(1, t+1):
    n, l = map(int, input().split())
    score = []
    kcal = []
    def dfs(index, taste, kcalo):
        global answer
        if kcalo > l:
            return
        if taste > answer:
            answer = taste
        if index == n:
            return
        dfs(index+1, taste+score[index], kcalo+kcal[index])
        dfs(index+1, taste, kcalo)
    for i in range(n):
        s, k = map(int, input().split())
        score.append(s)
        kcal.append(k)
    answer = 0
    dfs(0, 0, 0)
    print(f'#{tc} {answer}')