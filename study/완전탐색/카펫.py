def solution(brown, yellow):
    total = brown+yellow
    answer = []
    for b in range(1, total+1):
        if (total/b)%1 == 0:
            a = total//b
            if a*2+b*2 == brown+4:
                if a not in answer and b not in answer:
                    answer.append(a)
                    answer.append(b)
    return answer
                

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))