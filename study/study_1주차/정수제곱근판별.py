# def solution(n):
#     result = 0
#     for i in range(n):
#         if i*i == n:
#             result = i
#             i += 1
#             break
#         elif i*i > n:
#             return -1
#     answer = i*i
#     return answer
# -------------------------> 테스트케이스 마지막 불통과
# n이 1일 경우 고려

def solution(n):
    answer = 0
    num = n ** 0.5

    if num == int(num):
        answer = (num+1) ** 2
    else:
        return -1
    
    return answer