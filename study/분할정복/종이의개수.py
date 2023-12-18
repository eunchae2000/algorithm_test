n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = []

def solution(x, y, n):
    paper = arr[x][y]
    for i in range(x, n+x):
        for j in range(y, n+y):
            if paper != arr[i][j]:
                for a in range(3):
                    for b in range(3):
                        solution(x+a*n//3, y+b*n//3, n//3)
                return
    if paper == -1:
        answer.append(-1)
    elif paper == 0:
        answer.append(0)
    elif paper == 1:
        answer.append(1)

solution(0, 0, n)
print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))