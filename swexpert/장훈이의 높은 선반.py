# t = int(input())
# for tc in range(1, t+1):
#     n, b = map(int, input().split())
#     people = list(map(int, input().split()))
#     sum_list = [0]
#     for i in range(n):
#         for j in range(len(sum_list)):
#             result = people[i] + sum_list[j]
#             sum_list.append(result)
    
#     print(f'#{tc} {min([x-b for x in sum_list if x-b >= 0])}')

from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    people = list(map(int, input().split()))
    answer = 99999999
    for i in range(1, n+1):
        height = list(combinations(people, i))
        for j in height:
            if sum(j) >= b:
                if sum(j)-b < answer:
                    answer = sum(j)-b
    print(f'#{tc} {answer}')