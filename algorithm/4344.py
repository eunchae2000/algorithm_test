n = int(input())
answer=[]

for i in range(n):
    result = list(map(int, input().split()))
    res = result[0]
    if (result[0] != (len(result)-1)):
        break
    score = sum(result[1:])/res
    count = 0
    for j in range(res):
        if result[j+1] > score:
            count += 1
    r = count/res*100
    answer.append("%.3f"%r + "%")

for _ in answer:
    print(_)