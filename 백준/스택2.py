n = int(input())
stack = []
count = 0

for i in range(n):
    num = input().rstrip()
    
    if len(num) > 2:
        stack.append(int(num[2:]))
    elif num == '2'"