for tc in range(1, 11):
    T = int(input())
    N = input()
    stack = []
    result = []
    
    for i in N:
        if i.isdigit():
            result.append(i)
        elif i == '*':
            while stack and stack[-1] == '*':
                result.append(stack.pop())
            stack.append(i)
        elif i == '+':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    
    while stack:
        result.append(stack.pop())
    
    answer = []
    for i in result:
        if i == '+':
            answer.append(answer.pop() + answer.pop())
        elif i == '*':
            answer.append(answer.pop() * answer.pop())
        else:
            answer.append(int(i))
    print('#{} {}'.format(tc, stack.pop()))