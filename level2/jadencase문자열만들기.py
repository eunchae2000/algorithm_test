def solution(s):
    s_list = list(map(str, s.split(' ')))
    for i in range(len(s_list)):
        # capitalize : 맨 첫 글자만 대문자로 변경
        s_list[i] = s_list[i].capitalize()
    answer = ' '.join(s_list)
    return answer