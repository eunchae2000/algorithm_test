import sys
n = int(sys.stdin.readline())
for _ in range(n):
    arr = list(input())
    result = 0
    for i in arr:
        if i == '(':
            result += 1
        elif i == ')':
            result -= 1
        if result < 0 :
            print('NO')
            break
    
    if result == 0:
        print('YES')
    else:
        print('NO')