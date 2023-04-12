def solution(citations):
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        print(index, citation)
        if index >= citation:
            return index
    # h-index가 나올만큼 논문이 많지 않은 경우
    return len(citations)

print(solution([3, 0, 6, 1, 5]))