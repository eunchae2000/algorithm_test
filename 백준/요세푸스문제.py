n, k = map(int, input().split())
stack = list(range(1, n+1))
answer = []
num = 0

for i in range(n):
    num += (k-1)
    if num >= len(stack):
        num = num%len(stack)
    answer.append(str(stack.pop(num)))

print("<", ", ".join(answer[:]), ">", sep='')