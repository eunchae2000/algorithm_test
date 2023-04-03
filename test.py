def solution(clothes):
    dict = {}
    answer = 1
    for key, value in clothes:
        dict[value] = dict.get(value, 0) + 1
    
    for value in dict:
        answer *= dict[value] + 1
    
    return answer -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
