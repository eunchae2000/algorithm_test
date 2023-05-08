n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]
result = [0]*n

for i in range(n):
    for j in range(m):
        matrix1[i][j] += matrix2[i][j]

for a in matrix1:
    # *a는 배열의 괄호를 제거하고 출력
    print(*a)