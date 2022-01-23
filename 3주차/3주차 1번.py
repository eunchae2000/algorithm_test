N = int(input())

num = []

for i in range(N):
    a = input().split()
    if a[0] == 'push':
        num.append(a[1])
    elif a[0] == 'pop':
        if len(num) == 0:
            print(-1)
        else:
            print(num.pop())
    elif a[0] == 'size':
        print(len(num))
    elif a[0] == 'empty':
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(num) == 0:
            print("-1")
        else:
            print(num[0])
    elif a[0] == 'back':
        if len(num) == 0:
            print(-1)
        else:
            print(num[-1])