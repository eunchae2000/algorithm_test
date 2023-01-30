# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys

# sys.stdin.readline => 반복문으로 여러줄을 입력받는 상황에서 반드시 사용 / 이유: 시간 초과 발생x
n = int(sys.stdin.readline())
num_list = [0]*10001

# n개의 수를 입력받는 반복문
for i in range(n):
    num_list[int(sys.stdin.readline())] += 1
print(num_list)

# 배열의 수 만큼 반복문 돌리기
for j in range(10001):
    # num_list의 j 번째 숫자가 0이 아니면
    if num_list[j] != 0:
        for k in range(num_list[j]):
            print(j)

