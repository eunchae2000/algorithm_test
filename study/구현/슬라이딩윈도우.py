numbers = [1, 3, 2, 6, -1, 4, 1, 8, 2]
n = len(numbers)
k = 5

window = sum(numbers[:k])
answer = window

for i in range(k, n):
    window += numbers[i]-numbers[i-k]
    answer = max(answer, window)

print(answer)