import sys

n = int(sys.stdin.readline())
word = [sys.stdin.readline() for _ in range(n)]
word = list(set(word))

word.sort(key=lambda x:(len(x), x))

for i in word:
    for j in i:
        print(j, end="")