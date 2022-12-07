import re

def solution(today, terms, privacies):
    result = []
    for a in range(len(privacies)):
        privacies_list = privacies[a].split(" ")
        # date = privacies_list[a].split(".")
        print(privacies_list)
        for b in range(len(terms)):
            x = terms[b].split(" ")
            if (x[0] == privacies_list[1]):
                date = privacies_list[1].split(".")
                print(date)
            # ab = set(x[0])&set(privacies_list[a][1])
            # print(ab)
    
    
        
        # if x[0] == privacies_list[a]:

    # for i in range(len(terms_list),2):
    #     result.append(terms_list[i:i+2])
    #     print("result : " + result)
    # print(terms_list)
    # for i in range(len(terms)):
    #     for j in range(len(privacies)):
    #         a = set(terms_list[i])&set(privacies[j])

    answer = []
    return answer
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))