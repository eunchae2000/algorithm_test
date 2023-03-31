n, m = map(int, input().split())
box = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    box[a-1:b] = box[a-1:b][::-1]
    print(box)

print(*box)