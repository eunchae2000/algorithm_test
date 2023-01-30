# import math

# n = int(input())
# m = [list(map(int, input().split())) for _ in range(n)]
# result = 0

# for i in range(0, n-1):
#     for j in range(0, 1):
#         m[i][j] -= m[i][j+1]
#         m[i][j] -= m[i+1][j]

#         result += math.sqrt((m[i][j]* m[i][j]))
# print("%.2f" % result)

import math

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
# print(n)
# print(m)
result = 0

for i in range(0, n-1):
    x=m[i][0] - m[i+1][0]
    y=m[i][1] - m[i+1][1]

    result += math.sqrt((x**2)+(y**2))

print("%.2f" % result)
