t = int(input())        # 테스트 케이스 수

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = 0
    ho = 0
    if n % h == 0:
        floor = h*100
        ho = n//h
    else:
        floor = (n%h)*100
        ho = 1 + n//h
    print(floor+ho)