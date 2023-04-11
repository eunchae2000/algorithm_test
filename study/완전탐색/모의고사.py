def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for i, result in enumerate(answers):
        if one[i%5] == result:
            score[0] += 1
        if two[i%8] == result:
            score[1] += 1
        if three[i%10] == result:
            score[2] += 1
    
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))