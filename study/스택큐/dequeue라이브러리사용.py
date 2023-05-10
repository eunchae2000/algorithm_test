from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)

print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq)