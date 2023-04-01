n, m = map(int, input().split())
box = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (box[i]+box[j]+box[k]) > m:
                continue
            else:
                result = max(result , box[i]+box[j]+box[k])

print(result)
