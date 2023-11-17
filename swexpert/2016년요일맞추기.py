t = int(input())
cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, t+1):
    month, days = map(int, input().split())
    day = 0
    for i in range(month-1):
        day += cal[i]
    day += days
    answer = (day+4-1)%7
    print(f'#{tc} {answer}')