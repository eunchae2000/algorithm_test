def solution(n):
    answer = 0
    n = str(n)

    for i in range(len(n)):
        answer += int(n[i])

    return answer

# # 다른 사람 풀이
# def sum_digit(number):
#     if number < 10:
#         return number;
#     return (number % 10) + sum_digit(number // 10)