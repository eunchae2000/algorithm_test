def solution(name, yearning, photo):
    answer = []
    for photo_name in photo:
        score = 0
        for n in photo_name:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))