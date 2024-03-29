from itertools import combinations

def solution(number):
    nums = list(combinations(number, 3))
    answer = 0
    for i in nums:
        if sum(i) == 0:
            answer += 1
    return answer
print(solution([-2, 3, 0, 2, -5]))


# def solution(number):
#     answer = 0
#     for i in range(len(number)-2):
#         for j in range(i+1, len(number)-1):
#             for k in range(j+1, len(number)):
#                 if number[i] + number[j] + number[k] == 0:
#                     answer += 1
#     return answer