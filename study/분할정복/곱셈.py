a, b, c = map(int, input().split())

def solution(a, n):
    if n == 1:
        return a%c
    else:
        num = solution(a, n//2)
        if n%2 == 0:
            return (num*num)%c
        else:
            return (num*num*a)%c

print(solution(a, b))