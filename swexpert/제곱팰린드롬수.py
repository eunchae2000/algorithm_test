import math

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    answer = 0
    for i in range(n, m+1):
        num = i**(1/2)
        if num == int(num):
            i = str(i)
            num = str(int(num))
            if i == i[::-1] and num == num[::-1]:
                answer+=1
    print('#{}'.format(tc), answer)