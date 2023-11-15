for tc in range(1, 11):
    abc = input()
    answer = 0
    maps = []
    
    for _ in range(100):
        maps_list = list(map(int, input().split()))
        maps.append(maps_list)
    
    for i in range(100):
        result1, result2 = 0, 0
        for j in range(100):
            result1 += maps[i][j]
            result2 += maps[j][i]
        answer = max(result1, result2, answer)
    
    for i in range(100):
        result3, result4 = 0, 0
        result3 += maps[i][i]
        result4 += maps[i][99-i]
    answer = max(result3, result4, answer)
    
    print(f'#{tc} {answer}')