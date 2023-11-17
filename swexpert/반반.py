t = int(input())
for tc in range(1, t+1):
    string = input()
    s_list = list(set(string))
    if len(s_list) == 2:
        if string.count(s_list[0]) == 2 and string.count(s_list[1]) == 2:
            print(f'#{tc} {"Yes"}')
    else:
        print(f'#{tc} {"No"}')