from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for word in goal:
        if len(cards1) != 0:
            w = cards1[0]
            if w == word:
                answer += w
                cards1.popleft()
        if len(cards2) != 0:
            w = cards2[0]
            if w == word:
                answer += w
                cards2.popleft()
                
    if answer == ''.join(goal):
        return 'Yes'
    else:
        return 'No'

print(solution(["I", "drink", "water"], ["want", "to"], ["I", "want", "to", "drink", "water"]))
print(solution(["I", "water", "drink"], ["want", "to"], ["I", "want", "to", "drink", "water"]))