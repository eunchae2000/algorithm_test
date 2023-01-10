def solution(dartResult):
    n = []
    score = []
    answer = 0

    for i in dartResult:
        if i.isnumeric():
            n.append(int(i))
        elif i == 'S':
            n.append(int(n) ** 1)
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)** 2
            score.append(n)
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1] * 2
                score[-1] = score[-1] * -1
    return answer

print(solution('1S2D*3T'))

