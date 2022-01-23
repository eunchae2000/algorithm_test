from collections import deque

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0

    while queue:
        best = max(queue)
        front = queue.popleft()
        b -= 1

        if best == front:
            count += 1
            if b<0:
                print(count)
                break
        else:
            queue.append(front)
            if b<0:
                b = len(queue) -1
