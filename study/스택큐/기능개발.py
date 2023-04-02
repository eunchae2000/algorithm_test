def solution(progresses, speeds):
    count = 0
    time = 0
    answer = []
    while len(progresses) > 0:
        # 현재 작업량과 시간 * 한시간 작업량을 더해서 100이 넘는지 체크
        if (progresses[0] + speeds[0]*time) >= 100:
            # 작업 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer