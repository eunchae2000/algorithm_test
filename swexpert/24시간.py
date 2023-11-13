T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    answer = A + B
    if answer >= 24:
        answer -= 24
    else:
        answer = answer
        
    print('#{}'.format(tc), answer)