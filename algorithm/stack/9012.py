import sys

T = int(sys.stdin.readline())
stack = []

for i in range(T):
    input_data = input()
    data = list(input_data)
    result = 0

    for i in data:
        if i == '(':
            result += 1
        elif i == ')':
            result -= 1
        if result < 0:
            print("NO")
            break
    
    if result > 0:
        print("NO")
    elif result == 0:
        print("YES")