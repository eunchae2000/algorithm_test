t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    answer = 0
    small = min(a, b)
    answer = c//small
    if int(c%small) >= b:
        answer += (c//b)
    print(f'#{tc} {answer}')