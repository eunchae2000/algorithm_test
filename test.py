n = int(input())
m = int(input())
x = list(map(int, input().split()))
result = sum([i for i in range(n+1)])

count = 0

while True:
    count += 1
    answer = 0
    for i in x:
        if i-count < 0:
            answer += (i + (i+count))
        else:
            answer+= ((i-count) + i + (i+count))
            

    if result == answer:
        print(count)
        break
        