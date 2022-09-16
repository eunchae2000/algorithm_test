def solution(s):
    answer = ''
    s = list(map(int, s.split(" ")))
    print(s)
    list_a = []
    for i in range(len(s)):
        list_a.append(int(s[i]))
    answer = str(min(s)) + " " + str(max(s))

    return answer
