case = int(input())
def bit_count(n):
    count = 0
    while n>0:
        if n&1:
            count += 1
        n>>=1
    return count

def graduate(semester, taken):
    global n, k, m, l, memo, prerequisites, opened_lectures, MAX
    
    if bit_count(taken)>=k:
        return 0
    elif semester == m:
        return MAX
    
    if memo[semester][taken]:
        return memo[semester][taken]
    
    res = MAX
    can_take = opened_lectures[semester] & ~taken
    
    for i in range(n):
        if (can_take & (1<<i)) and (taken & prerequisites[i])!= prerequisites[i]:
            can_take &= ~(1<<i)
    take = can_take+1
    
    while take:
        take = (take-1) & can_take
        if bit_count(take) <= l:
            res = min(res, graduate(semester+1, taken|take)+1)
    
    res = min(res, graduate(semester+1, taken | take)+1)
    memo[semester][taken] = res
    return res

for _ in range(case):
    MAX = 987654321
    n, k, m, l = map(int, input().split())
    prerequisites = []
    for _ in range(n):
        pres = list(map(int, input().split()))[1:]
        pres_bit = 0
        for p in pres:
            pres_bit |= (1<<p)
        prerequisites.append(pres_bit)
    opened_lectures = []
    for _ in range(m):
        lectures = list(map(int, input().split()))[1:]
        lec_bit = 0
        for l in lectures:
            lec_bit |= (1<<l)
        opened_lectures.append(lec_bit)
    memo = [[0] * (1<<n) for _ in range(m)]
    answer = graduate(0, 0)
    
    if answer != MAX:
        print(answer)
    else:
        print("IMPOSSIBLE")