def solution(n):
    result = [0, 1]
    for i in range(n+1):
        result.append(result[-1]+result[-2])
    answer = result[n] % 1234567
    return answer