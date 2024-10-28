def solution(n, stages):
    challenger = [0]*(n+2)
    
    for i in stages:
        challenger[i] += 1
    
    print(challenger)
    
    fails = {}
    total = len(stages)
    
    for i in range(1, n+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i]/total
            total -= challenger[i]
    
    answer = sorted(fails, key=lambda x : fails[x], reverse=True)
    return answer
    
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))