import heapq


def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [],
    }
    print(dijkstra(graph, "A"))
