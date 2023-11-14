t = int(input())
for tc in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    answer = []
    answer.append(w*p)
    if r < w:
        answer.append(q +((w-r)*s))
    else:
        answer.append(q)
    print('#{}'.format(tc), min(answer))