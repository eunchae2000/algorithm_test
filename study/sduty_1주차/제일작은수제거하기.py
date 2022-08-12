def solution(arr):
    answer = []
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]


# def solution(arr):
#     answer = []
#     if type(arr) != int:
#         result = min(arr)
#         for i in range(len(arr)):
#             if arr[i] != result:
#                 answer.append(arr[i])
#     else:
#         return [-1]
#     return answer
# 테스트 케이스 : n이 10일 경우 통과 못함