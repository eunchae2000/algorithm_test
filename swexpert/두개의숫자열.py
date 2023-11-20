t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
        
    if len(A) > len(B):
        B, A = A, B
    
    arr = []
    for i in range(len(B)-len(A)+1):
        result = 0
        for j in range(len(A)):
            result += A[j]*B[i+j]
        arr.append(result)
    
    print(f'#{tc} {max(arr)}')
            
        
    