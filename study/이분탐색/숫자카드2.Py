n = int(input())
dic = {}
n_arr = list(map(int, input().split()))

for num in n_arr:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1

m = int(input())
m_arr = list(map(int, input().split()))
answer = []
for mNum in m_arr:
    if mNum not in dic:
        print(0, end=" ")
    else:
        print(dic[mNum], end=" ")