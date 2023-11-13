T = int(input())
for i in range(1, T+1):
    N = int(input())
    stack = set()
    count = 1
    while True:
        for j in list(str(N)):
            stack.add(j)
        if len(stack) == 10:
            break
        N //= count
        count += 1
        N *= count
    print('#{}'.format(i), N)