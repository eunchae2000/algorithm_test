def dfs(adj_matrix, start_node):
    num_nodes = len(adj_matrix)
    visited = [False] * num_nodes   # 방문한 노드를 표시하기 위한 배열
    stack = []
    
    stack.append(start_node)   # 시작 노드를 스택에 추가
    visited[start_node] = True   # 시작 노드를 방문 표시
    
    while stack:
        current_node = stack.pop()   # 스택에서 노드를 꺼냄
        print(current_node)   # 노드 방문 순서를 출력하거나 다른 작업을 수행
        
        for next_node in range(num_nodes):
            # 현재 노드와 연결된 인접한 노드를 찾음
            if adj_matrix[current_node][next_node] == 1 and visited[next_node]:
                stack.append(next_node)   # 스택에 추가
                visited[next_node] = True   # 방문 표시