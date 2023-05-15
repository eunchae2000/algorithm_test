t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    current = 0
    for i in arr[::-1]:
        if i >= current:
            current = i
        else:
            answer += current-i
    print("#", _+1 ," ", answer, sep="")