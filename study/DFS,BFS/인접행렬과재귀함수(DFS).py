def dfs(adj_matrix, current_node, visited):
    visited[current_node] = True   # 현재 노드를 방문 표시
    print(current_node)   # 노드 방문 순서를 출력하거나 다른 작업을 수행
    
    for next_node in range(len(adj_matrix[current_node])):
        # 현재 노드와 연결된 인접한 노드를 찾음
        if adj_matrix[current_node][next_node] == 1 and not visited[next_node]:
            # 재귀 호출
            dfs(adj_matrix, next_node, visited)

# 인접 행렬
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

num_nodes = len(adj_matrix)
# 방문한 노드를 표시하기 위한 배열
visited = [False] * (num_nodes)

# 각 노드를 시작 노드로 하여 DFS 수행
for start_node in range(num_nodes):
    if not visited[start_node]:
        dfs(adj_matrix, start_node, visited)