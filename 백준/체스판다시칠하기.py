n, m = map(int, input().split())
original = []
count = []

for _ in range(n):
    original.append(input())

for i in range(n-7):
    for j in range(m-7):
        w_board = 0;
        b_board = 0;
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if original[a][b] != 'W':
                        w_board += 1
                    if original [a][b] != 'B':
                        b_board += 1
                else:
                    if original[a][b] != 'B':
                        w_board += 1
                    if original [a][b] != 'W':
                        b_board += 1
        count.append(min(w_board, b_board))
print(min(count))