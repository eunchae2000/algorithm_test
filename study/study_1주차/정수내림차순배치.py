def solution(n):
    answer = ""
    n = list(str(n))
    n.sort(reverse=True)
    for i in n:
        answer += i
    return int(answer)

# 입력받은 정수들을 문자열의 리스트로 바꿔서 내림차순 정렬
# answer에 추가한 뒤 정수로 변환