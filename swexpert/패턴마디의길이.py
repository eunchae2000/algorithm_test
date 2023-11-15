t = int(input())
for tc in range(1, t+1):
    string = input()
    for i in range(1, len(list(string))):
        pattern = string[:i]
        if string[i:i+len(list(pattern))] == pattern:
            print('#{} {}'.format(tc, len(pattern)))
            break