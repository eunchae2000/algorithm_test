t = int(input())
for i in range(1, t+1):
    n, m =map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for a in range(n-m+1):
        for b in range(n-m+1):
            count = 0
            for c in range(m):
                for d in range(m):
                    count += arr[a+c][b+d]
            result.append(count)
    print("#{} {}".format(i, max(result)))