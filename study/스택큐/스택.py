import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    string = input().split()
    if string[0] == 'push':
        stack.append(int(string[1]))
    if string[0] == 'top':
        print(stack[-1])
    if string[0] == 'size':
        print(len(stack))
    if string[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if string[0] =='pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    