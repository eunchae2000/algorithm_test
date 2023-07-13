def solution(s):
    answer = []
    s = s[2:-2]
    string = s.split('},{')
    string.sort(key=len)
    for i in string:
        check = i.split(',')
        for j in check:
            if int(j) not in answer:
                answer.append(int(j))
    return answer