def solution(s):
    answer = 0
    for _ in range(len(s)):
        s_copy = s
        for j in range(len(s_copy)):
            if s_copy:
                s_copy = s_copy.replace('()', '')
                s_copy = s_copy.replace('{}', '')
                s_copy = s_copy.replace('[]', '')
        if not s_copy:
            answer += 1
        s = s[1:] + s[0]
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
