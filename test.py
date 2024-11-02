def board_table(m, n, board):
    table = []
    for i in range(n):
        temp = ''
        for j in range(m):
            temp += board[j][i]
        table.append(temp)
    return table

def crash(n, m, table, count = 0):
    crash_list = []
    
    for i in range(n-1):
        for j in range(m-1):
            default = table[i][j]
            if default == '0':
                pass
            elif default == table[i][j+1] and default == table[i+1][j] and default == table[i+1][j+1]:
                crash_list += [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
    crash_list = set(crash_list)
    
    if crash_list:
        for i, j in crash_list:
            table[i] = table[i][:j] + '0' + table[i][j+1:]
        for i in range(n):
            table[i] = table[i].replace('0', '')
            table[i] = '0' * (m-len(table[i])) + table[i]
        count += len(crash_list)
        return crash(n, m, table, count)
    else:
        return table, count

def solution(m, n, board):
    table = board_table(m, n, board)
    table, count = crash(n, m, table)
    return count

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))