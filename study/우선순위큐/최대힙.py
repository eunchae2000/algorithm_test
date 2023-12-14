import heapq

n = int(input())
stack = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(stack) == 0:
            print(0)
        else:
            max_num = max(stack)
            print(max_num)
            heapq.heappop(max_num)
    else:
        heapq.heappush(stack, num)