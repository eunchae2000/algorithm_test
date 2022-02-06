task = (list(map(int, input().split())))
speed = (list(map(int, input().split())))
result = []

while task:
    for i in range(len(task)):
        task[i] += speed[i]
    count = 0
    while task and task [0] >= 100:
        task.pop(0)
        speed.pop(0)
        count += 1
    if count > 0:
        result.append(count)

print(result)