import sys

n = int(sys.stdin.readline())
string = [sys.stdin.readline() for _ in range(n)]
string = list(set(string))

string.sort(key=lambda x:(len(x), x))

for i in string:
    for j in i:
        print(j, end="")