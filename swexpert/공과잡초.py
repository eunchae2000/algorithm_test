t = int(input())
for tc in range(1, t+1):
    garden = list(input())
    answer = 0
    for i in range(len(garden)-1):
        if garden[i] == '(':
            if garden[i+1] == '|':
                answer += 1
        
        if garden[i] == '|':
            if garden[i+1] == ')':
                answer += 1
        
        if garden[i] == '(' and garden[i+1] == ')':
            answer += 1
    
    print(f'#{tc} {answer}')
    