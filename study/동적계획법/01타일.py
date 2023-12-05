# 메모리 초과
# from itertools import permutations

# n = int(input())
# arr = ['00']*n + ['1']*n
# answer = []
# for i in range(1, n+1):
#     result = list(permutations(arr, i))
#     for res in result:
#         string = ''.join(res)
#         if len(string) == n:
#             answer.append(string)

# print(len(set(answer)))

import sys

input = sys.stdin.readline

n = int(input())
dp  =[0]*1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1])%15746
    
print(dp[n])