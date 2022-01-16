# 수가 주어지면 각 자리의 수를 내림차순으로 정렬해보자.

# 수를 입력
N = int(input())
# 입력받은 수를 int형을 str형으로 바꿔주고 리스트로 저장
num = list(map(int, str(N)))
# 해당 리스트를 내림차순으로 정렬해줌
num.sort(reverse=True)

# 정렬한 리스트를 하나씩 붙여서 출력
for i in num:
    print(i, end="")