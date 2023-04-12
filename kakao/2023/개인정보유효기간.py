def dateInfo(date):
    year, month, day = map(int, date.split('.'))
    return year*28*12 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    
    today = dateInfo(today)
    
    term_info = {}
    for term in terms:
        term = term.split()
        term_info[term[0]] = int(term[1])*28
    
    for info in range(len(privacies)):
        date, term = privacies[info].split()
        date = dateInfo(date)
        term = term_info[term]
        if today >= date+term:
            answer.append(info+1)
        
    return answer


print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))