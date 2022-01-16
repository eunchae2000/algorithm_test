n, m = map(int, input().split())

n = int(str(n)[::-1])
m = int(str(m)[::-1])

if n>m:
    print(n)
else:
    print(m)