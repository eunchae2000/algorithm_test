def solution(storey):
    answer = 0
    
    while storey:
        num1 = storey % 10
        num10 = (storey%100) // 10
        
        if num1 in [0, 1, 2, 3, 4]:
            answer += num1
        elif num1 == 5:
            if num10 in [0, 1, 2, 3, 4]:
                answer += num1
            elif num10 in [5, 6, 7, 8]:
                answer += (10-num1)
                storey += 10
        elif num1 in [6, 7, 8, 9]:
            answer += (10-num1)
            storey += 10
        storey = storey // 10
    return answer

print(solution(16))
print(solution(2554))