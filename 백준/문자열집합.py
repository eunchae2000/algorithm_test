n, m = map(int, input().split())
n_list = []
m_list = []

count = 0

for i in range(n):
    n_list.append(input())

for j in range(m):
    m_list.append(input())
    if m_list[j] in n_list:
        count += 1

print(count)