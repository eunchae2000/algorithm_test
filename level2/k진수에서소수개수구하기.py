def solution(n, k):
    num = ''
    answer = 0
    while n > 0:
        num = str(n%k)+num
        n //= k
    num = num.split('0')
    for i in num:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        prime = True
        for j in range(2, int(int(i)**0.5)+1):
            if int(i)%j == 0:
                prime = False
                break
        if prime:
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))