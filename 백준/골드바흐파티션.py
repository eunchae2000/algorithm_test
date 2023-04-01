era = [True] * 1000001 # 1000000 이하의 자연수
era[0] = era[1] = False # 0과 1은 소수가 아니기 때문에 제외

for i in range(1000001):    # 에라토스테네스의체 적용, 소수 리스트를 만들기 위해서
    if era[i]:
        for j in range(2*i, 1000001, i):
            era[j] = False

n = int(input())    # 횟수 입력
for k in range(n):
    num = int(input())
    count = 0       # 카운트 적용
    for _ in range(2, num//2+1):
        if era[_] and era[num-_]: # 모두 소수라면 카운트
            count += 1
    print(count)

