import sys

string = sys.stdin.readline()
bom = list(sys.stdin.readline().strip())

stack = []

for i in string:
    stack.append(i)
    if stack[-len(bom):] == bom and i == bom[-1]:
        del stack[-len(bom):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')