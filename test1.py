def solution(genres, plays):
    answer = []
    genre_dic = {}
    play_dic = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dic:
            genre_dic[genre] = []
            play_dic[genre] = 0
        genre_dic[genre].append((i, play))
        play_dic[genre] += play
    
    sort_arr = sorted(play_dic.items(), key=lambda x:-x[1])
    
    for genre, _ in sort_arr:
        sorted_song = sorted(genre_dic[genre], key=lambda x:(-x[1], x[0]))
        answer.extend(index for index, _ in sorted_song[:2])
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))