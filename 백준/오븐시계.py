h, m = map(int, input().split())
time = int(input())

h += (time) // 60
m += (time) % 60

if(m>= 60):
    h += int(m/60)
    m -= 60
if(h>= 24):
    h -= 24
print(h, m)