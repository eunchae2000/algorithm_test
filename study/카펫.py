# 런타임 에러
# def solution(brown, yellow):
#     for i in range(1, yellow+1):
#         for j in range(1, yellow+1):
#             if i + j == (brown-4)//2:
#                 if i*j == yellow:
#                     return j+2, i+2

def solution(brown, yellow):
    answer = brown + yellow
    for i in range(3, int(answer ** 0.5) + 1):
        if not answer % i and (i-2) * ((answer//i)-2) == yellow:
            return [answer//i, i]
