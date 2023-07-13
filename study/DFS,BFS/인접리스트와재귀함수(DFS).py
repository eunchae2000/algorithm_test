def dfs(adj_list, current_node, visited):
    visited[current_node] = True   # 현재 노드를 방문 표시
    print(current_node)   # 노드 방문 순서를 출력하거나 다른 작업을 수행 
    
    for next_node in adj_list[current_node]:
        if not visited[next_node]:
            dfs(adj_list, next_node, visited)   # 재귀 호출

# 인접리스트
adj_list = [
    [1, 2],
    [0, 3, 4],
    [0, 4],
    [1],
    [1, 2]
]

num_nodes = len(adj_list)
visited = [False] * num_nodes   # 방문한 노드를 표시하기 위한 배열

# 각 노드를 시작 노드로 하여 DFS 수행
for start_node in range(num_nodes):
    if not visited[start_node]:
        dfs(adj_list, start_node, visited)