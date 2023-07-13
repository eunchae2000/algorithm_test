from collections import deque

def bfs(adj_matrix, start_node):
    num_nodes = len(adj_matrix)
    visited = [False] * (num_nodes) # 방문한 노드를 표시하기 위한 배열
    queue = deque()   # 큐 생성
    
    queue.append(start_node)   # 시작 노드를 큐에 추가
    visited[start_node] = True  # 시작 노드를 방문 표시
    
    while queue:
        current_node = queue.popleft()   # 큐에서 노드를 꺼내옴
        print(current_node)   # 노드 방문 순서를 출력하거나 다른 작업 수행
        
        for next_node in range(num_nodes):
            # 현재 노드와 인접한 노드를 찾음(해당 배열이 1이고 방문하지 않은 상태)
            if adj_matrix[current_node][next_node] == 1 and not visited[next_node]:
                # 큐에 추가 
                queue.append(next_node)
                # 방문 표시
                visited[next_node] = True