# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
#  N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []

# 리스트 안에 숫자를 입력받고 오름차순으로 정렬
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()


# 배열의 상술평균을 구하기 위함
print(round(sum(num_list)/len(num_list)))
# num_list의 합을 sum을 이용하여 구하고 배열의 길이(len)로 나눈뒤 round를 이용하여 소수점 첫째자리로 반올림함

# 배열의 중앙값
print(num_list[len(num_list)//2])
# num_list의 길이(len)를 2로 나눈 몫의 정수 부분(// 연산자)의 수로 배열 순서를 구하여 출력


# 배열의 최빈값을 구하기 위함
cnt = Counter(num_list).most_common(2)
# Counter 클래스는 리스트에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려줌
# 또한 Counter의 most_common() 메소드는 등장한 횟수를 내림차순으로 정리해줌
# 만약 상위 3개의 결과만을 원한다면 most_common(3)을 하면 된다.

# 배열의 최빈값
if len(num_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 배열의 범위
print(max(num_list) - min(num_list))
# 배열의 최대값과 최솟값을 구해 최대값에서 최솟값을 뺀 결과를 출력