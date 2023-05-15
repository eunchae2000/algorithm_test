def dfs(change):
    global answer
    if not change:
        temp = (int(''.join(arr)))
        if answer < temp:
            answer = temp
        return
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            arr[i], arr[j] = arr[j], arr[i]
            temp_key = ''.join(arr)
            if visited.get((temp_key, change-1), 1):
                visited[(temp_key, change-1)] = 0
                dfs(change-1)
            arr[i], arr[j] = arr[j], arr[i]


t = int(input())
for i in range(t):
    answer = -1
    num, change = input().split()
    arr = list(num)
    arr_len = len(arr)
    visited = {}
    dfs(int(change))
    print("#{} {}".format(i+1, answer))