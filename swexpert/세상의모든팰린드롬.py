t = int(input())
for tc in range(1, t+1):
    string = input()
    answer = "Exist"
    if string == string[::-1]:
        answer = "Exist"
    else:
        for i in range(len(string)):
            if string[i] == '?':
                string[i] = string[len(string)-(i+1)]
            if string == string[::-1]:
                answer = "Exist"
            else:
                answer = "Not Exist"
    print(f'#{tc} {answer}')