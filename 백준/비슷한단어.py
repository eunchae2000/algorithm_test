import sys
n = int(sys.stdin.readline())
string = list(sys.stdin.readline())
answer = 0

for _ in range(n-1):
    compare = string[:]
    word = input()
    count = 0

    for i in word:
        if i in compare:
            compare.remove(i)
        else:
            count += 1
    if count<2 and len(compare) < 2:
        answer += 1

print(answer)