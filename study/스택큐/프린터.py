def solution(priorities,location):
    # 1. 튜플의 배열로 만들어줌
    printer = [(i, v) for i, v in enumerate(priorities)]
    turn = 0
    while printer:
        job = printer.pop(0)
        # job[1] => 튜플의 우선순위를 뽑을 수 있음 / 다른 작업과 우선순위를 비교 
        # 현재 작업보다 중요한 작업이 있는지 확인 / 없으면 printer의 맨뒤로 다시 추가
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            turn += 1
            # 현재 작업의 인덱스와 location의 값이 맞다면 출력
            if job[0] == location:
                break
    return turn


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))