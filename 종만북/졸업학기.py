# 테스트 케이스 수 입력받기
case = int(input())

def bit_count(n):
    count = 0
    while n>0:
        if n&1:
            count += 1
        n>>=1
    return count

def graduate(semester, taken):
    # 졸업까지 남은 학기 return
    global n, k, m, l, memo, prerequisites, opened_lectures, MAX
    
    # n 전공 과목 수, k 들어야 할 과목 수, m 학기 수, l 한 학기 당 최대 수강 과목 수
    
    # 이수 과목 수 >= 남은 과목 수
    # k개 이상의 과목을 이미 이수한 경우
    if bit_count(taken)>=k:
        # 졸업
        return 0
    
    # 이수 과목 수 < 남은 과목 수, 지난 학기 수 == 총 학기 수
    # m 학기가 전부 지난 경우, 남은 과목수가 있다 -> 졸업 x
    elif semester == m:
        return MAX
    
    # 아직 남은 학기가 있다.
    # memorization    
    if memo[semester][taken]:
        return memo[semester][taken]
    
    res = MAX
    # taken: 수강한 수업 bitmask
    # can_take: 수강한 수업의 bitmask를 이용하여 학기별 개설 과목 전체의 선수강 가능 여부 확인
    # 차집합을 이용해서 이번 학기에 들을 수 있는 과목 중 아직 듣지 않은 과목
    can_take = opened_lectures[semester] & ~taken
    
    # 선수 과목을 다 듣지 않은 과목들을 걸러낸다.
    for i in range(n):
        # 각 과목 별 '이번 학기 수강 가능' and '선수 과목을 수강하지 않음' -> 수강 불가
        if (can_take & (1<<i)) and (taken & prerequisites[i])!= prerequisites[i]:
            can_take &= ~(1<<i)
    take = can_take+1
    
    # while 문 내 take 모양 만들어주기 (take-1로 while 문 진행)
    while take:
        # 수강 가능한 과목을 하나씩 미수강
        take = (take-1) & can_take
        
        # 이번 학기 최대 수강 과목 수보다 적으면
        if bit_count(take) <= l:
            # 학기 이수, 경우의 수 진행
            # (taken | take) => 이전 학기 이수과목 + 이번 학기 이수 과목
            res = min(res, graduate(semester+1, taken|take)+1)
    
    # take == 0 일 경우 -> 이번 학기에 아무 것도 듣지 않을 경우
    res = min(res, graduate(semester+1, taken | take)+1)
    # memorization
    memo[semester][taken] = res
    return res

for _ in range(case):
    MAX = 987654321
    n, k, m, l = map(int, input().split())
    
    # prerequisites 수강해야 할 과목의 정보
    prerequisites = []
    for _ in range(n):
        pres = list(map(int, input().split()))[1:]
        # 선수 과목을 index로 하는 bitmask 생성
        pres_bit = 0
        for p in pres:
            pres_bit |= (1<<p)
        prerequisites.append(pres_bit)
    
    # opened_lectures 학기의 정보 (개설되는 과목의 번호)
    opened_lectures = []
    for _ in range(m):
        lectures = list(map(int, input().split()))[1:]
        # 개설되는 과목을 index로 하는 bitmask 생성
        lec_bit = 0
        for l in lectures:
            lec_bit |= (1<<l)
        opened_lectures.append(lec_bit)
    
    # 학기 * 전공 과목 수 만큼 2x2 memoArray 생성
    memo = [[0] * (1<<n) for _ in range(m)]
    answer = graduate(0, 0)
    
    if answer != MAX:
        print(answer)
    else:
        print("IMPOSSIBLE")