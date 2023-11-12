def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                burger.pop()
    
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))