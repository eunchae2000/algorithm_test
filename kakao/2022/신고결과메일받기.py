def solution(id_list, report, k):
    report_result = [0]*(len(id_list))
    result = {x: 0 for x in id_list}
    print(set(report))

    for i in set(report):
        a, b = i.split()
        result[b] += 1

    for i in set(report):
        a, b = i.split()
        if result[b] >= k:
            report_result[id_list.index(a)] += 1
    return report_result

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))