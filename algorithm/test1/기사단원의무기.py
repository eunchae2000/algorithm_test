# 시간초과
# def solution(number, limit, power):
#     answer = 0
#     for i in range(1, number+1):
#         count = 0
#         for j in range(1, i+1):
#             if i%j == 0:
#                 count += 1
#         print(count)
#         if count > limit:
#             answer += power
#         else:
#             answer += count

#     return answer

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                count += 1
                if j**2 != i:
                    count += 1
            if count > limit:
                count = power
                break
        answer += count
    return answer
    

print(solution(5, 3, 2))
print(solution(10,3,2))