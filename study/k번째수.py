def solution(array, commands):
    new_arr = []
    answer = []
    for i, j, k in commands:
        new_arr = array[i-1 : j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer