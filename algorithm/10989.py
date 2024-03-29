# 정렬

def merge_sort(array):
    # array의 배열이 1보다 작으면 리턴
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid]) #왼쪽부터 mid까지
    right = merge_sort(array[mid:]) #mid부터 오른쪽까지 

    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

# 데이터 입력
n=int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)