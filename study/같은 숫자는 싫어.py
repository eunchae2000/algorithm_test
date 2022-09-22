def solution(arr):
    answer = []
    for i in range(len(arr)-1): 
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
            if i+1 == len(arr)-1:
                answer.append(arr[i+1])
        else:
            if i+1 == len(arr)-1:
                answer.append(arr[i+1])
    return answer

# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a