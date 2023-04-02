import heapq

def solution(s, k):
    heap = []
    count = 0
    # s의 원소들을 heapq를 사용하여 heap에 저장
    for i in s:
        heapq.heappush(heap, i)

    while heap[0]<k:
        # heap은 원소를 추가하거나 삭제하면 자동으로 정렬해주기 때문에 원소를 추가하고 정렬은 굳이 선언x
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        count += 1

        # 예외
        if len(heap) == 1 and heap[0] < k:
            return -1
    return count