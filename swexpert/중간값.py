import math
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[math.ceil(len(arr)/2)-1])
