N, M = map(int, input().split())

solve = []

def DFS(depth):
    if depth == M:
        for i in solve:
            print(i, end=" ")
        print()
        return
    # 1부터 N까지 중에서
    for i in range(1, N+1):
        # solve에 i가 없으면
        if i not in solve:
            # solve에 i를 추가
            solve.append(i)
            # depth에 1을 증가시켜주면서 M과 같아 질 때까지 증가시켜줌
            DFS(depth + 1)
            # solve에서 하나를 빼줌
            solve.pop()
DFS(0)