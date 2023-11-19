t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    
    result = "Possible"
    for i in range(n):
        bread = (people[i]//m)*k-(i+1)
        if bread < 0:
            result = "Impossible"
            break
    
    print(f'{tc} {result}')