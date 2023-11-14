for i in range(1, 11):
    n = int(input().split())
    puzzle = [list(input() for _ in range(8))]
    answer = 0
    
    for y in range(8):
        for x in range(8-n+1):
            A = puzzle[y][x:x+n]
            if A == A[::-1]:
                answer += 1
    
    
    for x in range(8):
        for y in range(8-n+1):
            A = ''
            for z in range(y, y+n):
                A += puzzle[z][x]
            if A == A[::-1]:
                answer += 1
        
    
    print('#{}'.format(i), answer)