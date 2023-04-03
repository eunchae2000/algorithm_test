def solution(nums):
    poket = len(set(nums))
    if len(nums)//2 > poket:
        return poket
    return len(nums)//2
    