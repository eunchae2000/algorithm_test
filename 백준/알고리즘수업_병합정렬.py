import sys
input = sys.stdin.readline

def merge_sort(arr):
    global answer
    
    if len(arr) == 1:
        return arr
    
    mid = (len(arr)+1)//2
    
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    result = []
    left, right = 0, 0
    
    while left<len(left_arr) and right < len(right_arr):
        if left_arr[left] <  right_arr[right]:
            result.append(left_arr[left])
            answer.append(left_arr[left])
            left += 1
        else:
            result.append(right_arr[right])
            answer.append(right_arr[right])
            right += 1
    
    result += left_arr[left:]
    answer += left_arr[left:]
    
    result += right_arr[right:]
    answer += right_arr[right:]
    
    return result

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
merge_sort(arr)

if len(answer) >= k:
    print(answer[k-1])
else:
    print(-1)