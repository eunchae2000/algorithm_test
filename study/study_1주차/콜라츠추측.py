def solution(num):
    answer = 0
    # 입력받은 정수가 1일 경우를 고려하지 않아 테스트 케이스 불통과
    if num == 1:
        return 0
    
    while (True):
        if num % 2 == 0:
            num /= 2
        else:
            num = (num*3) + 1
        answer += 1
        if num == 1:
            return answer
        elif answer == 500:
            return -1

    return answer