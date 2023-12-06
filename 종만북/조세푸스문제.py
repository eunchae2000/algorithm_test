def josephus(n, k):
    survivors = list(range(1, n+1))
    kill = 0
    
    while n > 2:
        survivors.pop(kill)
        n -= 1
        kill = (kill + k -1) %n
    print(survivors[0], survivors[1])

c = int(input())
for i in range(c):
    n, k = map(int, input().split())
    josephus(n, k)