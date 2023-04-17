def solution(numbers):
    answer = []
    result = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

# from itertools import combinations
# def solution(numbers):
#     answer = set()
#     for i in list(combinations(numbers, 2)):
#         answer.add(sum(i))
#     return answer