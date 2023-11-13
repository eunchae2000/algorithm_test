def solution(x):
    answer = []
    temp = 0
    zero = 0
    while True:
        if x == 1:
            break
        zero += x.count('0')
        x = x.replace('0', '')
        x = bin(len(x))[2:]
        temp += 1
    answer = [temp, zero]
    return answer