n, m = map(int, input().split())
basket = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        basket[b-1] = k

for c in range(n):
    print(basket[c], end=" ")
