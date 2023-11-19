t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    m = list(map(int, bin(m)[2:]))
    m.reverse()
    
    if m[:n].count(1) == n:
        print(f'#{tc} {"ON"}')
    else:
        print(f'#{tc} {"OFF"}')