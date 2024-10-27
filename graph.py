import heapq
from collections import defaultdict
from typing import Dict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list

    def add_edge(self, u: int, v: int, weight: int):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def dijkstra(self, start: int) -> Dict[int, float]:
        """
        Finds the shortest paths from the start vertex to all other vertices.
        """
        min_heap = [(0, start)]  # (distance, vertex)
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            # If the distance is greater than the recorded, skip
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Testing the Graph and Dijkstra's algorithm


def main():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)

    start_vertex = 0
    shortest_paths = g.dijkstra(start_vertex)

    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Vertex {vertex}: {distance}")
    print("Test run success")


if __name__ == "__main__":
    main()
