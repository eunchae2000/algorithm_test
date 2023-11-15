t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    s = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    answer = []
    result = 0
    for i in range(n):
        score = 0
        a, b, c = map(int, input().split())
        score += ((a*0.35)+(b*0.45)+(c*0.2))
        answer.append(score)
    result = answer[k-1]
    answer.sort(reverse=True)
    div = n//10
    print(f'#{tc} {s[answer.index(result)//div]}')
    
    