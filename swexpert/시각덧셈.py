t = int(input())
for tc in range(1, t+1):
    a, b, c, d = map(int, input().split())
    time = 0
    minute = 0

    if (b+d) >= 60:
        minute = (b+d)-60
        time += 1
    else:
        minute = b+d
    
    if (a+c) >= 13:
        time += (a+c-12)
    else:
        time += (a+c)
    
    print(f'#{tc} {time} {minute}')