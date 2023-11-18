from itertools import combinations, permutations

t = int(input())
for tc in range(1, t+1):
    num = list(map(int, input().split()))
    num_list = list(combinations(num, 3))
    answer = []
    for i in range(len(num_list)):
        answer.append(sum(num_list[i]))
    answer = list(set(answer))
    answer.sort(reverse=True)
    print('#{} {}'.format(tc, answer[4]))