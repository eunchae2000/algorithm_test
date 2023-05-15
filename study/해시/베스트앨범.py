def solution(genres, plays):
    genre_dic = {}
    play_index_dic = {}
    answer = []

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dic:
            genre_dic[genre] = play
        else:
            genre_dic[genre] += play
        if genre not in play_index_dic:
            play_index_dic[genre] = [(i, play)]
        else:
            play_index_dic[genre].append((i, play))
    for (key, value) in sorted(genre_dic.items(), key=lambda x:x[1], reverse=True):
        for (index, play) in sorted(play_index_dic[key], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(index)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))