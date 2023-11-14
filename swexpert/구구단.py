T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a>=10 or b>=10:
        print("#{}".format(tc), -1)
    else:
        print("#{}".format(tc), a*b)