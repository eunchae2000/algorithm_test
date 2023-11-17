t = int(input())
for tc in range(1, t+1):
    code = [list(input()) for _ in range(5)]
    answer = ''
    max_len = 0
    for c in code:
        if len(c) > max_len:
            max_len = len(c)

    for i in range(max_len):
        for j in range(5):
            if i<len(code[j]):
                answer += code[j][i]
    print(answer)