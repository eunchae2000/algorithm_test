import sys
input = sys.stdin.readline

n = int(input())
stack = []
count = 0

for i in range(n):
    num = input().rstrip()
    
    if len(num) > 2:
        stack.append(int(num[2:]))
    elif num == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif num == '3':
        print(len(stack))
    elif num == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif num == '5':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)