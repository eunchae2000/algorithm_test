T = int(input())
for i in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    result = sum(num)//n
    count = 0
    for people in num:
        if people <= result:
            count += 1
    print('#{}'.format(i), count)