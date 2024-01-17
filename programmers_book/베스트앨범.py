def solution(genres, player):
    answer = []
    genres_dic = {}
    player_dic = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = player[i]
        if genre not in genres_dic:
            genres_dic[genre] = []
            player_dic[genre] = 0
        genres_dic[genre].append((i, play))
        player_dic[genre] += play
    
    sorted_genre = sorted(player_dic.items(), key=lambda x:x[1], reverse=True)
    
    for genre, _ in sorted_genre:
        sorted_song = sorted(genres_dic[genre], key=lambda x:(-x[1], x[0]))
        answer.extend(index for index, _ in sorted_song[:2])
        
    return answer
        
    
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))