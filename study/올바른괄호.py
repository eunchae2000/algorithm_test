def solution(s):
    answer = 0
    for i in range(len(s)):
        if s[i] == '(':
            answer+=1
        if s[i] == ')':
            if answer > 0:
                answer -= 1
            else:
                return False
            
    if answer == 0:
        return True
    else:
        return False