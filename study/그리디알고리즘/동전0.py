n, money = map(int, input().split())
m = list(int(input()) for _ in range(n))
m.sort(reverse=True)
answer = 0

for coin in m:
    answer += money//coin
    money %= coin

print(answer)
    