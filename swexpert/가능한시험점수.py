# from itertools import combinations, permutations

# t = int(input())
# for tc in range(1, t+1):
#     answer = 1
#     n = int(input())
#     question = list(map(int, input().split()))
#     q = set(question)
#     if len(q) == 1:
#         answer += len(question)
#     else:
#         answer += len(q)
#         for i in range(2, len(q)):
#             combi = list(combinations(q, i))
#             answer += len(combi)
#     print('#{}'.format(tc), answer)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    question = list(map(int, input().split()))
    result = [0]
    temp = [0]
    for i in range(n):
        for a, b in enumerate(result):
            temp.append(result[a]+question[i])
        result = list(set(temp))
    print(f'#{tc} {len(result)}')
        