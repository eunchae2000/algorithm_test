for i in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    print('#{}'.format(tc), n**m)