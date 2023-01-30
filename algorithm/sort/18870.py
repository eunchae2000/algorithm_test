# import sys

# n = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))

# num_list = sorted(set(num))

# dic_list = {num_list[i]: i for i in range(len(num_list))}

# for i in num:
#     print(dic_list[i], end=" ")

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# num 리스트의 중복을 제거한 뒤 오름차순으로 정렬하고 num_list에 저장
num_list = sorted(set(num))

# num_list의 순서대로 dictionary 자료형을 사용하여 num_list 순서대로 key 값과 value 값을 할당하여 dic_list에 저장 
dic_list = {num_list[i]: i for i in range(len(num_list))}

# dic_list의 value 값을 num 리스트 순서대로 출력
for i in num:
    print(dic_list[i], end=" ")