import sys
input = sys.stdin.readline

def merge_sort(l):
    if len(l) == 1:
        return l
    
    mid = (len(l)+1)//2
    
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    
    i, j = 0, 0
    l2 = []
    
    while i<len(left) and j <len(right):
        if left[i] < right[j]:
            l2.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            l2.append(right[j])
            answer.append(right[j])
            j += 1
    while i<len(left):
        l2.append(left[i])
        answer.append(left[i])
        i+=1
    while j<len(right):
        l2.append(right[j])
        answer.append(right[j])
        j+=1
    return l2
            
n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
merge_sort(arr)

if len(answer) >= k:
    print(answer[k-1])
else:
    print(-1)