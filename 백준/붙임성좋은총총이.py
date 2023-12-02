n = int(input())
here = {'ChongChong'}

for i in range(n):
    a, b = input().split()
    if a in here:
        here.add(b)
    if b in here:
        here.add(a)

print(len(here))