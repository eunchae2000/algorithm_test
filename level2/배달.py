import heapq

def solution(N, road, K):
    graph = {i: [] for i in range(N+1)}
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    def dijkstra(start):
        distances = {i: float('inf') for i in range(N+1)}
        distances[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for idj, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[idj]:
                    distances[idj] = distance
                    heapq.heappush(queue, (distance, idj))
        return distances
    distances = dijkstra(1)
    answer = sum(1 for distance in distances.values() if distance <= K)
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))