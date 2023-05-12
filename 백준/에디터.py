import sys
string_left = list(sys.stdin.readline().rstrip())
string_right = []
m = int(sys.stdin.readline())

for _ in range(m):
    word = sys.stdin.readline().split()
    if word[0] == 'L' and string_left:
        string_right.append(string_left.pop())
    elif word[0] == 'D' and string_right:
        string_left.append(string_right.pop())
    elif word[0] == 'B' and string_left:
        string_right.pop()
    elif word[0] == 'P':
        string_left.append(word[1])

print("".join(string_left+list(reversed(string_right))))