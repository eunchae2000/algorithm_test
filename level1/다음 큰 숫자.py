def solution(n):
    nNum = bin(n).count('1')
    for i in range(n+1, 1000001):
        if nNum == bin(i).count('1'):
            return i

print(solution(78))
print(solution(15))