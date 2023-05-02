def solution(player, calling):
    play_dict = {play:index for index, play in enumerate(player)}
    index_dict = {index:play for index, play in enumerate(player)}

    for i in calling:
        current_index = play_dict[i]
        front_index = current_index-1

        current_play = i
        front_play = index_dict[front_index]
        
        play_dict[current_play], play_dict[front_play] = front_index, current_index
        index_dict[current_index], index_dict[front_index] = front_play, current_play
    return list(index_dict.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))