n = int(input())
for tc in range(1, n+1):
    number = list(map(int, input().split()))
    count = 0
    for i in range(1, len(number)-1):
        for j in range(i+1, len(number)):
            if number[i] > number[j]:
                number[i], number[j] = number[j], number[i]
                count += 1
    print(number[0], count)