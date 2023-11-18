t = int(input())
for tc in range(1, t+1):
    stick = input()
    stack = []
    answer = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append('(')
        else:
            if stick[i-1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
    print(f'#{tc} {answer}')
