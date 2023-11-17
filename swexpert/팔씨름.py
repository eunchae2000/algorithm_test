t = int(input())
for tc in range(1, t+1):
    result = input()
    result_len = len(result)
    if result.count('x') <= 7:
        print(f'#{tc} {"YES"}')
    else:
        print(f'#{tc} {"NO"}')
        