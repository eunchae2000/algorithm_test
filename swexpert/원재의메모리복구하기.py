T = int(input())
for i in range(1, T+1):
    memory = input()
    N = "0"
    count = 0
    
    for j in range(len(memory)):
        if memory[j] != N:
            N = memory[j]
            count += 1
    print('#{}'.format(i), count)
    
    
