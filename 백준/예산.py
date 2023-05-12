import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start, end = 0, max(arr)
total = 0

while start <= end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        if i <= mid:
            total += i
        else:
            total += mid
    if total <= m:
        start = mid+1
    else:
        end = mid-1

print(end)