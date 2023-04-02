import heapq
def solution(operations):
    answer = []
    heap = []

    for i in range(len(operations)):
        if i[0] == 'I':
            heapq.heappush(heap, int(i[2:]))
        else:
            if len(heap) == 0:
                pass
            elif i[2] == '-':
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    
    if len(heap):
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer
