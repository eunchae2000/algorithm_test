def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n) % 26 + ord('a'))
            answer += s[i]
        elif s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n) % 26 + ord('A'))
            answer += s[i]
        else:
            answer += ' '

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))