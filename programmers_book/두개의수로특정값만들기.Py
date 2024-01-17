def count_arr(arr, k):
    hashArr = [0]*(k+1)
    for a in arr:
        if a<= k:
            hashArr[a] = 1
    return hashArr

def solution(arr, target):
    hashArr = count_arr(arr, target)
    
    for num in arr:
        n = target-num
        if (n != num and
            hashArr[n] == 1 and
            n >= 0 and n<=target):
            return True
    return False

print(solution([1, 2, 3, 4, 8], 6))
print(solution([2, 3, 5, 9], 10))
