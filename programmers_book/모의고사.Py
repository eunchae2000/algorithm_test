def solution(answers):
    students = [[1, 2, 3, 4, 5],
           [2, 1, 2, 3, 2, 4, 2, 5],
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0]*3
    for i, answer in enumerate(answers):
        for j, student in enumerate(students):
            if answer == student[i%len(student)]:
                scores[j] += 1
    
    max_socre = max(scores)
    result = []
    for i, score in enumerate(scores):
        if score == max_socre:
            result.append(i+1)
    return result

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))