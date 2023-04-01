import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_list = sorted(list(set(num)))

num_dict = {}

for i in range(len(num_list)):
    num_dict[num_list[i]] = i

for i in num:
    print(num_dict[i], end=" ")