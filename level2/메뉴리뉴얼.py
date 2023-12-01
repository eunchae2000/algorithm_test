from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            combi = combinations(sorted(order), c)
            menu += combi
        counter = Counter(menu)
        print(counter)
        print(counter.values())
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(word) for word in counter if counter[word] == max(counter.values())]
            
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
