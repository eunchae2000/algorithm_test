def solution(x):
    answer = True
    num = 0
    for i in str(x):
        num += int(i)
    
    if int(x) % num == 0:
        answer = True
    else:
        answer = False

    return answer

# def Harshad(n):
#     # n은 하샤드 수 인가요?
#     return n % sum([int(c) for c in str(n)]) == 0