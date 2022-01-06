# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하세요.

# 입력받을 수의 개수를 입력받음
N = int(input())
# N개의 수를 입력받아 리스트로 저장
num = [list(map(int, input().split())) for _ in range(N)]

# 리스트를 오름차순으로 정렬
num.sort()

# 리스트의 요소를 하나씩 출력
for i in num:
    for j in i:
        print(j)