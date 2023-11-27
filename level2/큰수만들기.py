def solution(number, k):
    answer = []
    
    while k>0 and answer and answer[-1]<number:
        answer.pop()
        k -= 1
    answer.append()

    return answer