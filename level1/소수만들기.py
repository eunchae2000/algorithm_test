from itertools import combinations  

def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):  
            if num%n == 0:
                return False
        return True

def solution(nums):
    answer = 0
    combination = list(combinations(nums, 3))
    for arr in combination:
        if prime(sum(arr)):
            answer += 1
    return answer

print(solution([1, 2, 7, 6, 4]))
