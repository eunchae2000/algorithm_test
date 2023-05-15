import math
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    answer = 0
    print("# {}".format(i+1))
    for j in range(len(arr)):
        answer += arr[j]
    print((answer/len(arr)))