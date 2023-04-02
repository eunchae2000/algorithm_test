def solution(arr):
    answer = []
    for i in range(len(arr)):
        # 마지막 원소까지 확인해주기 위해서 첫번째 값은 동일하게 넣어줌
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer