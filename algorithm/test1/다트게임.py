def solution(dartResult):
    score = []
    answer = 0
    dartResult = dartResult.replace('10', 't')
    
    
    for i in dartResult:
        if i.isnumeric():
            answer += int(i)
            continue
        elif i == 't':
            answer += 10
            continue
        elif i == 'S':
            score.append(answer)
        elif i == 'D':
            score.append(answer**2)
        elif i == 'T':
            score.append(answer**3)
        elif i == '*':
            if len(score) > 1:
                score[-1] *= 2
                score[-2] *= 2
            else:
                score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
        answer = 0
    
    return sum(score)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
