def solution(s):
    answer = []
    words = {}

    for index, word in enumerate(s):
        if word not in words:
            answer.append(-1)
            words[word] = index
        else:
            answer.append(index-words[word])
            words[word] = index
    return answer