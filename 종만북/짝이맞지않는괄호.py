t = int(input())
dic = {')':'(', '}':'{', ']':'['}
for _ in range(t):
    string = list(input())
    stack = []
    for i in string:
        if i in "({[":
            stack.append(i)
        else:
            if (stack):
                top = stack.pop()
                if dic[i] != top:
                    break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")