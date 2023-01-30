#!! 방법 1!!#
#def solution(array, commands):
#    answer = []
#    for command in commands:
#        i, j, k = command[0], command[1], command[2]
#        slice = array[i-1:j]
#        slice.sort()
#        answer.append(slice[k-1])
#    return answer

#!!! 방법 2 !!!#
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]], commands))