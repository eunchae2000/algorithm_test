import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        # 처리할 작업이 있는 경우
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            # 작업 요청 시간부터 종료시간까지의 시간 계산
            answer += now - cur[1]
            i += 1
        # 처리할 작업이 없는 경우 다음 작업으로 넘어감
        else:
            now += 1
            print(now)
    return answer // len(jobs)
    