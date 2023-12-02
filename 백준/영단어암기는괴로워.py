import sys

n, m = map(int, sys.stdin.readline().split())
answer = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    
    if len(word) < m:
        continue
    else:
        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1

answer = sorted(answer.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in answer:
    print(i[0])