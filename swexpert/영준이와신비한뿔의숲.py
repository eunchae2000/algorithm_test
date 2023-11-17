t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    answer = 2*m-n
    print(f'#{tc} {answer} {m-answer}')