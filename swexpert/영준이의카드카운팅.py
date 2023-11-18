t = int(input())
for tc in range(1, t+1):
    str = input()
    answer = [13, 13, 13, 13]
    length = 3
    str_list = [str[0+i:length+i] for i in range(0, len(str), length)]
    if len(str_list) != len(set(str_list)):
        print('#{} {}'.format(tc, 'ERROR'))
        continue
    for s in str_list:
        if 'S' in s:
            print(s)
            answer[0] -= 1
        elif 'D' in s:
            answer[1] -= 1
        elif 'H' in s:
            answer[2] -= 1
        elif 'C' in s:
            answer[3] -= 1
    print(f'#{tc}', end=" ")
    print(*answer)
            