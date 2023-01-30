# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

n = input()

def result(n):
    return (''.join(sorted(n)[::-1]))
# sorted로 n을 정렬하고, 뒤집어 줘야하기 때문에 [::-1]을 사용해서 거꾸로 출력하고 join으로 연결해준다
# (''.join(reversed(sorted(n)))) <- 이것도 가능

print(result(n))