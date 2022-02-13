dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

num = input()
count = 0

for i in range(len(num)):
    for j in dial:
        if num[i] in j:
            count += dial.index(j) + 3
print(count)