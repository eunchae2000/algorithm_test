t = int(input())
for i in range(1, t+1):
    n = int(input())
    grades = list(map(int, input().split()))
    score = [0]*101
    current = 0
    for num in grades:
        score[num] += 1
        if score[num] >= score[current]:
            current = num
    print(f"#{i} {current}")