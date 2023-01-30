# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split())))
    # 2차원 배열을 한 번에 입력받는 방법

num_list.sort(key=lambda x:(x[1],x[0]))
# lambda는 우선순위를 정해주는 함수
# key 인자에 함수를 넘겨주어 x의 값을 비교하여 정렬해줌
# x[1], x[0]은 2차원 배열의 뒷 부분 먼저 비교한 뒤 겹치는 숫자가 생기면 앞부분을 비교하여 정렬해줌

for i in num_list:
    print(i[0], i[1])