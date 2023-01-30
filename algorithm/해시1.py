# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     num = len(completion)
#     for i in range(num):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[num]

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))