N = int(input())
num = 1
stack = []
result = []

for i in range(1, N+1):
    data = int(input())
    # num이 data보다 작으면 1부터 data까지 추가
    while num<=data:
        stack.append(num)
        num += 1
        result.append('+')
    # stack의 최상위 값이 data와 같으면 pop
    if stack[-1] == data: 
        stack.pop()
        result.append('-')
    # 수열을 만들기 불가능한 경우
    else: 
        print('NO')
        exit(0)   

print('\n'.join(result)) 