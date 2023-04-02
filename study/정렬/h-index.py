def solution(citations):
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        print(index, citation)
        if index >= citation:
            return index
    return len(citations)

print(solution([3, 0, 6, 1, 5]))