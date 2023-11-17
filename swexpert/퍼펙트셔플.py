t = int(input())
for tc in range(1, t+1):
    num = int(input())
    shuffle = list(input().split())
    answer = ''
    if num%2 == 0:
        n = num//2
        string1 = shuffle[:n]
        string2 = shuffle[n:]
        for i in range(len(string1)):
            answer += string1[i] + ' '
            answer += string2[i] + ' '
    else:
        n = num//2+1
        string1 = shuffle[:n]
        string2 = shuffle[n:]
        for i in range(len(string2)):
            answer += string1[i] + ' '
            answer += string2[i] + ' '
        answer += string1[-1]
    print(f'#{tc} {answer}')