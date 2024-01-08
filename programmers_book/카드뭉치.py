from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for word in goal:
        if cards1 and cards1[0] == word:
            answer += cards1[0]
            cards1.popleft()
        if cards2 and cards2[0] == word:
            answer += cards2[0]
            cards2.popleft()
                
    if answer == ''.join(goal):
        return 'Yes'
    else:
        return 'No'

print(solution(["I", "drink", "water"], ["want", "to"], ["I", "want", "to", "drink", "water"]))
print(solution(["I", "water", "drink"], ["want", "to"], ["I", "want", "to", "drink", "water"]))