def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for x, y in zip(A, B):
        answer += x*y
    return answer

# return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))