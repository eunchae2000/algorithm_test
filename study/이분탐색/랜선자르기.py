k, n = map(int, input().split())
arr = []
for _ in range(k):
    num = int(input())
    arr.append(num)
    
min_num = 1
max_num = max(arr)

while min_num <= max_num:
    mid = (min_num+max_num)//2
    lan = 0
    for i in arr:
        lan += i//mid
    if lan >= n:
        min_num = mid+1
    else:
        max_num = mid-1
    
print(max_num)