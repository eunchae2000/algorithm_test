# import sys

# n, m = map(int, sys.stdin.readline().split())
# memo = []
# blog = []
# for _ in range(n):
#     memo_string = sys.stdin.readline()
#     memo.append(memo_string)

# for i in range(m):
#     blog_string = list(sys.stdin.readline().split(','))
#     for m in memo:
#         if m in blog_string:
#             memo.pop()
#     print(len(memo))

import sys
n, m = map(int, sys.stdin.readline().split())
board = dict()
for _ in range(n):
    board[sys.stdin.readline().rstrip()] = 1

    res = n
    for _ in range(m):
        count = sorted(sys.stdin.readline().rstrip().split(','))
        for c in count:
            if c in board.keys():
                if board[c] == 1:
                    board[c] -= 1
                    res -= 1
        print(res)