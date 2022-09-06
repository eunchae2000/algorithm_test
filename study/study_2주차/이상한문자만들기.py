def solution(s):
    result = s.split(" ")

    for i in range(len(result)):
        s_list = list(result[i])

        for j in range(len(s_list)):
            if j % 2 == 1:
                s_list[j] = (s_list[j].lower())
            elif j % 2 == 0:
                s_list[j] = (s_list[j].upper())
        result[i] = "".join(s_list)

    answer = " ".join(result)
    return answer

print(solution("try hello world"))

def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))