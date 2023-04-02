def solution(s):
    answer = []
    for i in s:
        if i == '(':
            answer.append(0)
        else:
            if len(answer) == 0:
                return False
            else:
                answer.pop()
    
    if len(answer) != 0:
        return False
    else:
        return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))