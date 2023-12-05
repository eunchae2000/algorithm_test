import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = [1]*1000001
    for j in range(3, n+1):
        arr[j] = arr[j-2]+arr[j-3]
    
    print(arr[n-1])
    