def solution(n, stages):
    people = len(stages)
    answer = {}
    for i in range(1, n+1):
        num = stages.count(i)
        result = num/people
        answer[i] = result
        people -= num
    
    return sorted(answer, key=lambda x:-answer[x])

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4]))


# def solution(n, stages):
#     challenger = [0]*(n+2)
#     for stage in stages:
#         challenger[stage] += 1
    
#     fails = {}
#     total = len(stages)
    
#     for i in range(1, n+1):
#         if challenger[i] == 0:
#             fails[i] = 0
#         else:
#             fails[i] = challenger[i]/total
#             total -= challenger[i]
#     result = sorted(fails, key=lambda x:fails[x], reverse=True)