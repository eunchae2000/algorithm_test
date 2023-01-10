from math import sqrt

def solution(n):
    num = set(range(2, n+1))
    for i in range(2, int(sqrt(n+1))+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)
    # return num

print(solution(10))
print(solution(5))

# 다시
# def solution(n):
#     count = 0
#     num = 0

#     for i in range(1, n+1):
#         count = 0
#         for j in range(1, i+1):
#             if i == 1:
#                 pass
#             else:
#                 if i%j == 0:
#                     count+=1
#         if count>1 and count<=2:
#             num += 1
#     return num