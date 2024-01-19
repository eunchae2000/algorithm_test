from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = []
        for o in orders:
            combi = combinations(sorted(o), c)
            menu += combi
        count = Counter(menu)
        if len(count) != 0 and max(count.values()) != 1:
            for m, cnt in count.items():
                if cnt == max(count.values()):
                    answer.append(''.join(m))
    return sorted(answer)

print(solution(["ABCEG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))