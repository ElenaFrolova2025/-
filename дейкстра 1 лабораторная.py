import sys
import heapq

def dijkstra(graph, start):

    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}


    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)


        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def reconstruct_route(predecessors, start, end):
    route = []
    current_node = end

    while current_node != start:
        route.append(current_node)
        current_node = predecessors[current_node]

    route.append(start)
    route.reverse()

    return route


graph = {
    'A': {'B': 3, 'C': 7, 'D': 13},
    'B': {'A': 3, 'C': 5, 'D': 9},
    'C': {'A': 7, 'B': 5, 'D': 11},
    'D': {'A': 13, 'B': 9, 'C': 11}
}
start_node = 'A'
end_node = 'B'
end_node1 = 'C'
end_node2 = 'D'

distances, predecessors = dijkstra(graph, start_node)

route = reconstruct_route(predecessors, start_node, end_node)
route1 = reconstruct_route(predecessors, start_node, end_node1)
route2 = reconstruct_route(predecessors, start_node, end_node2)

print(f"Кратчайшее расстояние от начальной точки {start_node} до {end_node}: {distances[end_node]}")
print(f"Маршрут: {route}")

print(f"Кратчайшее расстояние от начальной точки {start_node} до {end_node1}: {distances[end_node1]}")
print(f"Маршрут: {route1}")

print(f"Кратчайшее расстояние от начальной точки {start_node} до {end_node2}: {distances[end_node2]}")
print(f"Маршрут: {route2}")