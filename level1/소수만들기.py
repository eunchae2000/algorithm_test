from itertools import combinations  # 중복 허용x

def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):  # math 함수를 사용x
            if num%n == 0:
                return False
        return True

def solution(nums):
    answer = 0
    combination = list(combinations(nums, 3)) # nums 배열을 3개씩 조합하여 list로 변경
    for arr in combination:
        if prime(sum(arr)):
            answer += 1
    return answer

print(solution([1, 2, 7, 6, 4]))
