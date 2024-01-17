def solution(record):
    dic = {}
    answer = []
    for i in record:
        arr = i.split()
        if arr[0] == 'Enter' or arr[0]=='Change':
            dic[arr[1]] = arr[2]
    
    for i in record:
        arr = i.split()
        if arr[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %dic[arr[1]])
        elif arr[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %dic[arr[1]])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
        