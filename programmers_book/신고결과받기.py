def solution(id_list, report, k):
    reported_dic = {}
    result = {}
    
    for i in report:
        uid, rid = i.split()
        if rid not in reported_dic:
            reported_dic[rid] = set()
        reported_dic[rid].add(uid)
    
    for report_list, user_list in reported_dic.items():
        if len(user_list) >= k:
            for user in user_list:
                if user not in result:
                    result[user] = 1
                else:
                    result[user] += 1
    
    answer = []
    for i in range(len(id_list)):
        if id_list[i] not in result:
            answer.append(0)
        else:
            answer.append(result[id_list[i]])
    return answer
        
        
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))