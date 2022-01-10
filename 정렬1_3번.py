import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()

# 산술평균
print(round(sum(num_list)/len(num_list)))

# 중앙값
print(num_list[len(num_list)//2])

# 최빈값
cnt = Counter(num_list).most_common()
if len(num_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위
print(max(num_list) - min(num_list))