n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

first = arr[-1]
second = arr[-2]

count = int(m//k)*k
answer = (first*count) + (second*(m-count))
print(answer)
