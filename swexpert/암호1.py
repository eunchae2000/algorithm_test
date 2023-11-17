for tc in range(1, 11):
    n = int(input())
    code = list(map(int, input().split()))
    com = int(input())
    command = list(input().split())
    
    for i in range(len(command)):
        if command[i] == 'I':
            index = int(command[i+1])
            num = int(command[i+2])
            for j in range(num):
                command.insert(index+j, int(command[i+2+(j+1)]))
    
    print('#{} {}'.format(tc, ' '.join(map(str, command[:10]))))