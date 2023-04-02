import heapq

# heapify => 기존 리스트를 힙으로 변경


def solution(operations):
    answer = []
    heap = []
    
    for data in operations:
        # 연산이 I일 경우
        if data[0] == 'I':
            heapq.heappush(heap, int(data[2:]))
        # 연산이 D일 경우
        else:
            if len(heap) == 0:
                pass
            # 공백 뒤가 "-"일 경우 최소힙을 제거
            elif data[2] == '-':
                heapq.heappop(heap)
            # 공백 뒤가 아무것도 아닐 경우
            else:
                # 힙에서 가장 큰 수를 제외화고 다시 힙에 넣음
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    
    if len(heap):
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer