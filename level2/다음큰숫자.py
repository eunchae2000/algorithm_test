def solution(n):
    num = bin(n).count('1')
    for i in range(n+1, 1000001):
        if num == bin(i).count('1'):
            return i