def solution(n, lost, reserve):
    num = [i for i in range(1, n+1)]
    result = n-len(lost)
    for i in range(len(reserve)):
        if reserve[i] in lost:
            pass
        elif reserve[i] !=1:
            if (reserve[i]-1) in lost or (reserve[i]+1) in lost :
                result += 1
    return result
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(4, [2, 3], [3, 4]))