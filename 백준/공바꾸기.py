n, m = map(int, input().split())
box = []
for i in range(n):
    box.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    box[a-1], box[b-1] = box[b-1], box[a-1]

for _ in range(n):
    print(box[_], end=" ")

