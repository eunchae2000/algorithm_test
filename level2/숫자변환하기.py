from collections import deque

def solution(x, y, n):
    queue = deque()
    visited = set()
    
    queue.append((x, 0))
    
    while queue:
        i, j = queue.popleft()
        
        if i>y or i in visited:
            continue
        visited.add(i)
        if i == y:
            return j
        for k in (i*3, i*2, i+n):
            if k <= y and k not in visited:
                queue.append((k, j+1))
    return -1


def solution2(x, y, n):
    visited = set()
    min_operations = float('inf')  # 최소 연산 횟수를 저장하는 변수

    # DFS 재귀 함수 정의
    def dfs(i, operations):
        nonlocal min_operations
        if i > y or i in visited or operations >= min_operations:
            return
        if i == y:
            min_operations = min(min_operations, operations)
            return

        visited.add(i)
        
        # DFS 탐색: 가능한 연산을 통해 y에 도달하는지 확인
        dfs(i * 3, operations + 1)
        dfs(i * 2, operations + 1)
        dfs(i + n, operations + 1)
        
        visited.remove(i)  # 백트래킹

    # DFS 시작
    dfs(x, 0)

    # min_operations가 갱신된 경우만 반환
    return min_operations if min_operations != float('inf') else -1



print(solution2(10, 40, 5))
print(solution2(10, 40, 30))
print(solution2(2, 5, 4))