def solution(sizes):
    answer = max(max(x)for x in sizes) *  max(min(x) for x in sizes)
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))