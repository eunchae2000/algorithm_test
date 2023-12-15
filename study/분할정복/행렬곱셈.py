a1, a2 = map(int, input().split())
alist = []
for _ in range(a1):
    num = list(map(int, input().split()))
    alist.append(num)

b1, b2 = map(int, input().split())
blist = []
for _ in range(b1):
    num = list(map(int, input().split()))
    blist.append(num)

answer = [[0 for _ in range(b2)] for _ in range(a1)]

for i in range(a1):
    for j in range(b2):
        for k in range(b1):
            answer[i][j] += alist[i][k]*blist[k][j]

for a in answer:
    for b in a:
        print(b, end=" ")
    print()