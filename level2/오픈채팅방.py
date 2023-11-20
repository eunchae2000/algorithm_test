def solution(record):
    answer = []
    dic = {}
    
    for word in record:
        sentence = word.split()
        if len(sentence) == 3:
            dic[sentence[1]] = sentence[2]
    
    for word in record:
        sentence = word.split()
        if sentence[0] == "Enter":
            answer.append('%s님이 들어왔습니다.' %dic[sentence[1]])
        elif sentence[0] == "Leave":
            answer.append('%s님이 나갔습니다.' %dic[sentence[1]])
    return answer