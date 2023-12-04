def merge_sort(arr):
    global answer
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    answer = []
    left, right = 0, 0
    
    while left<len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            answer.append(left_arr[left])
            left += 1
        else:
            answer.append(right_arr[right])
            right += 1
            
    answer += left_arr[left:]
    answer += right_arr[right:]
    
    return answer

            