n, m = map(int, input().split())
num = list(map(int, input().split()))
sum_arr = [0, num[0]]

for i in range(1, len(num)):
    sum_arr.append(sum_arr[i]+num[i])

for i in range(m):
    a, b = map(int, input().split())
    print(sum_arr[b]-sum_arr[a-1])