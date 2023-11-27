m = ['a', 'e', 'i', 'o', 'u']

while True:
    string = input()
    answer = 1
    count = 0
    if string == 'end':
        break
    for i in m:
        if i in string:
            count += 1
    if count < 1:
        print(f'<{string}> is not acceptable.')
        continue
    for i in range(len(string)-2):
        if string[i] in m and string[i+1] in m and string[i+2] in m:
            answer = 0
        elif not (string[i] in m) and not (string[i+1] in m) and not (string[i+2] in m):
            answer = 0
    if answer == 0:
        print(f'<{string}> is not acceptable.')
        continue
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            if string[i] == 'e' or string[i] == 'o':
                continue
            else:
                answer = 0
    
    if answer == 0:
        print(f'<{string}> is not acceptable.')
        continue
    print(f'<{string}> is acceptable.')