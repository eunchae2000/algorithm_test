n, m = map(int, input().split())

n_list = set()
for i in range(n):
    n_list.add(input())

m_list = set()
for j in range(m):
    m_list.add(input())

info = sorted(list(n_list & m_list))

print(len(info))

for k in info:
    print(k)