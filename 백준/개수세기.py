num = int(input())
number = list(map(int, input().split()))
find = int(input())
count = 0

for i in range(num):
    if(number[i] == find):
        count += 1

print(count)