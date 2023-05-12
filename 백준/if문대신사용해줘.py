import sys
n, m = map(int, sys.stdin.readline().split())
rank = [(sys.stdin.readline().split()) for _ in range(n)]
def solution(rank, number):
    start, end = 0, len(rank)-1
    result = 0
    while start <= end:
        mid = (start+end)//2
        if int(rank[mid][1]) >= number:
            end = mid-1
            result = mid
        else:
            start = mid+1
    return result

for i in range(m):
    count = int(sys.stdin.readline())
    print(rank[solution(rank, count)][0])
