n = int(input())
arr = list(map(int, input().split()))
mode = list(map(int, input().split()))

maxi = -1e9
mini = 1e9

def dfs(depth, total, plus, minus, multi, divine):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    if plus:
        dfs(depth+1, total+arr[depth], plus-1, minus, multi, divine)
    if minus:
        dfs(depth+1, total-arr[depth], plus, minus-1, multi, divine)
    if multi:
        dfs(depth+1, total*arr[depth], plus, minus, multi-1, divine)
    if divine:    
        dfs(depth+1, int(total/arr[depth]), plus, minus, multi, divine-1)

dfs(1, arr[0], mode[0], mode[1], mode[2], mode[3])

print(maxi)
print(mini)        