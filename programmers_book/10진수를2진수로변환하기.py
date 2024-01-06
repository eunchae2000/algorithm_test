def solution(decimal):
    answer = []
    while True:
        if decimal == 0:
            break
        else:
            num = int(decimal%2)
            decimal //= 2
            answer.append(num)
    n = answer[::-1]
    return ''.join(str(a) for a in n)

print(solution(10))
print(solution(27))
print(solution(12345))