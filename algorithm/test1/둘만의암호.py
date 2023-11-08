# def solution(s, skip, index):
#     answer = ''
#     array = list(skip)
#     for s_word in s:
#         ss = []
#         for i in range(1, index+1):
#             ss.append(chr(ord(s_word)+i))
        
#         for j in ss:
#             if j in array:
#                 if (ord(ss[-1])+1) > 122:
#                     ss.append(chr(ord(ss[-1])-26))
#                 if (ord(ss[-1])+1) <= 122:
#                     ss.append(chr(ord(ss[-1])+1))
#                 ss.remove(j)
#             print(ss)
#         answer += ss[-1]
        
#     return answer

def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    # 중복된 문자 제거
    for ch in skip:
        if ch in alpha:
            alpha = alpha.replace(ch, "")
    
    # index만큼 뒤에 있는 알파벳 저장
    for i in s:
        change = alpha[(alpha.index(i)+index)%len(alpha)]
        answer += change
    return answer


print(solution("aukks", "wbqd", 5))