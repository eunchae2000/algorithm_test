def solution(park, routes):
    x = 0
    y = 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
                break
    
    for move in routes:
        x_move = x
        y_move = y
        for step in range(int(move[2])):
            if move[0] == 'E' and y_move < len(park[0])-1 and park[x_move][y_move+1] != 'X':
                y_move += 1
                if step == int(move[2])-1:
                    y = y_move
            if move[0] == 'W' and y_move > 0 and park[x_move][y_move-1] != 'X':
                y_move -= 1
                if step == int(move[2])-1:
                    y = y_move
            if move[0] == 'S' and x_move < len(park[0])-1 and park[x_move+1][y_move] != 'X':
                x_move += 1
                if step == int(move[2])-1:
                    x = x_move
            if move[0] == 'N' and x_move > 0 and park[x_move-1][y_move] != 'X':
                x_move -= 1
                if step == int(move[2])-1:
                    x = x_move
    return [x, y]


print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))