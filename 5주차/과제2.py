num = int(input())

for i in range(num):
    n, m = map(str, input().split())
    for i in m:
        print(i*int(n), end="")
    print()