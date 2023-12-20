# n = int(input())
# n_arr = list(map(int, input().split()))
# m = int(input())
# m_arr = list(map(int, input().split()))

# for i in m_arr:
#     if i in n_arr:
#         print(1)
#     else:
#         print(0)

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()

for num in m_arr:
    left, right = 0, n-1
    isAnswer = False
    
    while left<=right:
        mid = (left+right)//2
        if num == n_arr[mid]:
            isAnswer = True
            print(1)
            break
        elif num > n_arr[mid]:
            left = mid+1
        else:
            right = mid-1
    if not isAnswer:
        print(0)