def solution(N, stages):
    result = {}
    answer = []
    number = len(stages)

    for i in range(1, N+1):
        if number !=0:
            count = stages.count(i)
            result[i] = count/number
            number -= count
        else:
            result[i] = 0
    answer = sorted(result, key=lambda x : result[x], reverse=True)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))