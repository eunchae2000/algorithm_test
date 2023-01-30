# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))
    # 2차원 배열의 요소들을 한 번에 입력받는 방법

num_list.sort()
# 배열을 오름차순으로 정렬

# 배열을 하나씩 출력하기 위해서 따로 반복문 돌리기
for i in num_list:
    for j in i:
        print(j, end=' ')
    print()