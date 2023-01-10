def solution(n, lost, reserve):
    fstudent = set(lost) - set(reserve)
    astudent = set(reserve) - set(lost)

    for i in astudent:
        if i-1 in fstudent:
            fstudent.remove(i-1)
        elif i+1 in fstudent:
            fstudent.remove(i+1)
    return n-len(fstudent)
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(4, [2, 3], [3, 4]))