num = list(map(int, input().split()))
origin = [1, 1, 2, 2, 2, 8]

for i in range(6):
    if(num[i] == origin[i]):
        num[i] = 0
    else:
        num[i] = origin[i]-num[i]

for _ in range(6):
    print(num[_], end=" ")