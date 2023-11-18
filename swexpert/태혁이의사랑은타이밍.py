t = int(input())
for tc in range(1, t+1):
    day, time, minute = map(int, input().split())
    day_result = (day-11)*24*60
    time_result = (time-11)*60
    minute_result = (minute-11)
    answer = day_result+time_result+minute_result
    
    if time == 11 and minute == 11:
        answer = 0
    elif day == 11 and time < 11:
        answer = -1
        
    print(f'#{tc} {answer}')