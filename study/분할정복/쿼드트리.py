n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

def solution(x, y, n):
    tree = arr[x][y]
    for i in range(x, n+x):
        for j in range(y, n+y):
            if tree != arr[i][j]:
                tree = -1
                break
    if tree == -1:
        print("(", end="")
        solution(x, y, n//2)
        solution(x, y+n//2, n//2)
        solution(x+n//2, y, n//2)
        solution(x+n//2, y+n//2, n//2)
        print(")", end="")
    elif tree == 1:
        print(1, end="")
    elif tree == 0:
        print(0, end="")
        
solution(0, 0, n)