t = int(input())
for i in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    row_arr = arr
    col_arr = [[arr[a][b] for a in range(9)] for b in range(9)]
    sqr_arr = [[arr[a%3*3+b//3][a//3*3+b%3] for b in range(9)] for a in range(9)]
    answer = 1
    for row, col, sqr in zip(row_arr, col_arr, sqr_arr):
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9:
            continue
        else:
            answer = 0
            break
    print("#{} {}".format(i, answer))