T = int(input())
for i in range(T):
    num = int(input())
    race = list(map(int, input().split()))
    up = [0]
    down = [0]
    for j in range(0, len(race)-1):
        numA = race[j]
        numB = race[j+1]
        if numA < numB:
            up.append(numB-numA)
        elif numA > numB:
            down.append(numA-numB)
    print('#{}'.format(i+1), [max(up), max(down)])