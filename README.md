# Dijkstra

## Complexity

- Best: O(V^2 + E)
- Worst: O(V^2 + E)
- Avg: O(V^2 + E)
- Space: O(V + E)

## Problem Description

Dijkstra's algorithm finds the shortest path distances from one start vertex to every reachable vertex in a weighted graph with non-negative edge weights. Instead of trying every possible route, the algorithm builds the correct distances one step at a time by always focusing on the currently closest unfinished vertex.

This implementation keeps a set of unvisited vertices and repeatedly selects the unvisited vertex with the smallest tentative distance before relaxing its outgoing edges. The important restriction is that all edge weights must be non-negative. If negative edges are allowed, the greedy decision that Dijkstra relies on is no longer guaranteed to stay correct.

## Code

```javascript
/**
 * Compute shortest-path distances from a start node with Dijkstra's algorithm.
 *
 * This implementation finds the next vertex by scanning the unvisited set,
 * so its runtime is O(V^2 + E) instead of the priority-queue variant.
 *
 * @param {Object.<string, Array<[string, number]>>} graph Weighted adjacency list.
 * @param {string} start Starting node label.
 * @returns {{distances: Record<string, number>}} Final distance table.
 */
function dijkstra(graph, start) {
    const distances = {};
    const unvisitedNodes = new Set();

    for (const node in graph) {
        distances[node] = Infinity;
        unvisitedNodes.add(node);
    }

    distances[start] = 0;

    while (unvisitedNodes.size > 0) {
        let current = null;

        // Pick the unvisited node with the smallest tentative distance.
        for (const node of unvisitedNodes) {
            if (current === null || distances[node] < distances[current]) {
                current = node;
            }
        }

        if (current === null || distances[current] === Infinity) {
            break;
        }

        // Relax every outgoing edge from the current node.
        for (const [neighbor, weight] of graph[current]) {
            if (!unvisitedNodes.has(neighbor)) {
                continue;
            }

            const candidateDistance = distances[current] + weight;

            if (candidateDistance < distances[neighbor]) {
                distances[neighbor] = candidateDistance;
            }
        }

        unvisitedNodes.delete(current);
    }

    return { distances };
}

/**
 * Run the Dijkstra demonstration on a small weighted graph.
 *
 * @returns {void}
 */
function main() {
    const graph = {
        A: [["B", 4], ["C", 2]],
        B: [["A", 4], ["C", 1], ["D", 5]],
        C: [["A", 2], ["B", 1], ["D", 8], ["E", 10]],
        D: [["B", 5], ["C", 8], ["E", 2], ["F", 6]],
        E: [["C", 10], ["D", 2], ["F", 3]],
        F: [["D", 6], ["E", 3]],
    };

    console.log("Original graph =", JSON.stringify(graph));
    console.log("Start node =", "A");
    console.log("Shortest paths =", dijkstra(graph, "A"));
}

main();
```

## Algorithm Steps

1. Initialize every vertex distance to infinity except the start vertex, which begins at 0.
2. Place every vertex in the unvisited set.
3. Repeatedly choose the unvisited vertex with the smallest tentative distance.
4. For each outgoing edge from that vertex, test whether the path through the current vertex produces a shorter distance to the neighbor.
5. If the new path is shorter, update the neighbor's stored distance.
6. Remove the current vertex from the unvisited set because its shortest distance is finalized.
7. Continue until no unvisited vertices remain.

## Explanation

The greedy idea behind Dijkstra's algorithm is that once the algorithm selects the unvisited vertex with the smallest tentative distance, that distance is final, provided all edge weights are non-negative. No later path can come back and improve it, because any alternative path would have to pass through a vertex that is already at least as far away.

After choosing the current vertex, the algorithm examines each outgoing edge and performs relaxation. That means it checks whether going through the current vertex gives a shorter path to a neighbor than the best path recorded so far. If it does, the stored distance for that neighbor is updated. Repeating that process causes the correct shortest-path distances to spread outward from the start vertex.

This version does not use a priority queue. Instead, it scans the entire unvisited set each round to find the next vertex to process. That selection step costs `O(V)` each time, so the full implementation runs in `O(V^2 + E)` time. The graph representation and distance table together use `O(V + E)` space.
