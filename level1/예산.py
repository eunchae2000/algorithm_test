def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
    return answer
