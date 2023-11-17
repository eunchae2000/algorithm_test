t = int(input())
for tc in range(1, t+1):
    num = int(input())
    shuffle = list(input().split())
    answer = ''
    string1 = shuffle[:num//2]
    string2 = shuffle[num//2:]
    for i in range(len(string1)):
        answer += string1[i] + ' '
        answer += string2[i] + ' '
    if num % 2 != 0:
        answer += shuffle[-1]
    print(f'#{tc} {answer}')