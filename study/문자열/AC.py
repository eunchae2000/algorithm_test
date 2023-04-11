from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(",")
    queue = deque(arr)

    count = 0

    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            count += 1
        elif i == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if count % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")