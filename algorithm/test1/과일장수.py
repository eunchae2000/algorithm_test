def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        apple = score[i:i+m]
        if len(apple) == m:
            answer += min(apple)*m
    return answer
print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))