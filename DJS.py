import heapq

def dijkstra(graph, start):
    # 初始化距离字典，起点的距离为0，其他点为正无穷
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 最小堆用于获取当前最小距离的节点
    pq = [(0, start)]  # (距离, 节点)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # 如果当前节点的距离已经大于已知最短距离，跳过
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 如果新计算的距离更小，则更新最短距离并将邻居加入堆中
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# 图的表示：节点与邻居的边及权重
graph = {
    'A': [('B', 10), ('C', 5)],  # A -> B=10, A -> C=5
    'B': [('A', 10), ('C', 4), ('D', 3)],  # B -> A=10, B -> C=4, B -> D=3
    'C': [('A', 5), ('B', 4), ('D', 2)],  # C -> A=5, C -> B=4, C -> D=2
    'D': [('B', 3), ('C', 2)]   # D -> B=3, D -> C=2
}

# 从A出发计算最短路径
start = 'D'
distances = dijkstra(graph, start)
print(f"从 {start} 到其他城市的最短距离: {distances}")

