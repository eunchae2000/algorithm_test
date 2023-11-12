def solution(wallpaper):
    answerA = []
    answerB = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                answerA.append(i)
                answerB.append(j)
    return [min(answerA), min(answerB), max(answerA)+1, max(answerB)+1]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))