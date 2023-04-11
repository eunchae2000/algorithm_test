import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [-1, 1, 0, 0]
ans = 0

def bfs():
    # (0, 0) 출발, 벽 안부순 상태 시작
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위 안에 있고, 한 번도 방문하지 않았으면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[nx][ny][wall] + 1
                
                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nx][ny] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nx, ny, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로 + 1 저장
                    visited[nx][ny][1] = visited[x][y][wall] + 1

    return -1


print(bfs())