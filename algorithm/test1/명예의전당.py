def solution(k, score):
    top3 = []
    answer = []
    for i in score:
        if len(top3)<k:
            top3.append(i)
        else:
            if min(top3)<i:
                top3.remove(min(top3))
                top3.append(i)
        answer.append(min(top3))
    return answer
print(solution(3,[10, 100, 20, 150, 1, 100, 200]))