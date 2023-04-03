# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

def solution(participant, completion):
    dict = {}
    result = 0
    for part in participant:
        dict[hash(part)] = part
        result += hash(part)
    
    for com in completion:
        result -= hash(com)
    
    return dict[result]