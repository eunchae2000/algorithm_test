import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

answer = []

def solution(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)
solution(0, 0, n)
print(answer.count(0))
print(answer.count(1))