t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f = [x for x in range(1, num+1)]
    for i in range(floor):
        for j in range(1, num):
            f[j] += f[j-1] 
    print(f[-1])