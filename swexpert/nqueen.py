def possible(index, count):
    for i in range(index):
        if index-i == abs(count-arr[i]):
            return True
    return False

def queen(index):
    global answer
    if index == n:
        answer += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        if possible(index, i):
            continue
        visited[i] = 1
        arr[index] = i
        queen(index + 1)
        visited[i] = 0

t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = 0
    queen(0)
    print("#{} {}".format(i, answer))
