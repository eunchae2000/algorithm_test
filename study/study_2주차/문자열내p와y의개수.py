def solution(s):
    answer = True
    x = 0
    y = 0
    
    for i in range(len(s)):
        if (s[i] == 'p' or s[i] == 'P'):
            x += 1
        elif(s[i] == 'y' or s[i] == 'Y'):
            y += 1
    
    if x == y:
        answer = True
    elif x == 0 and y == 0:
        answer = True
    else:
        answer = False
    
    return answer

# def numPY(s):
#     문자열을 전부 소문자로 바꾸고 p와 y의 개수를 각각 카운트해서 갯수를 비교
#     return s.lower().count('p') == s.lower().count('y')
