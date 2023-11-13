T = int(input())
dic = ['a', 'e', 'i', 'o', 'u']
for i in range(1, T+1):
    string = input()
    for j in string:
        if j in dic:
            string = string.replace(j, '')
    print('#{}'.format(i), string)