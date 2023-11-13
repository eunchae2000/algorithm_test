T = int(input())
for i in range(1, T+1):
    num = int(input())
    answer = 0
    for j in range(1, num+1):
        if j%2==0:
            answer -= j
        else:
            answer += j
    print('#{}'.format(i), answer)