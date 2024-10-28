from collections import Counter

def solution(str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1_lower)-1):
        if str1_lower[i].isalpha() and str1_lower[i+1].isalpha():
            str1_list.append(str1_lower[i]+str1_lower[i+1])
    for j in range(len(str2_lower)-1):
        if str2_lower[j].isalpha() and str2_lower[j+1].isalpha():
            str2_list.append(str2_lower[j]+str2_lower[j+1])
    
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int((len(inter)/len(union))*65536)
    
print(solution("FRANCE", "french"))