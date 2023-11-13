def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer = 0
    for x, y in zip(A, B):
        answer += x*y
    return answer