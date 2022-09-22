def solution(n):
    count = 0
    for i in range(1, 1+n):
        answer = 0
        for j in range(i, n+1):
            answer += j
            if answer == n:
                count+= 1
                break
            else:
                if answer>n:
                    break
    return count

print(solution(15))