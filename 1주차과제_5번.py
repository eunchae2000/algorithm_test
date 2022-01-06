# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y 좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성

# 입력받을 개수 입력
n = int(input())
# n개의 숫자를 입력받고 리스트에 저장
num = [list(map(int, input().split())) for _ in range(n)]

# 먼저 첫번째 수와 비교하여 정렬하고 첫번째수가 같다면 두번째 수와 비교하여 오름차순으로 정렬
num.sort(key=lambda x:(x[0], x[1]))

# 리스트의 요소를 하나씩 출력
for i in num:
    for j in i:
        print(j, end=" ")
    print()