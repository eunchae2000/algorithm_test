# def solution(n):
#     count = 0
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i%j == 0:
#                 break
#         else:
#             count += 1
#     return count

# 에라토스테네스 체를 이용
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

print(solution(10))
print(solution(5))