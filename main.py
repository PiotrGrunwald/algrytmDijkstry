from heapq import heappop, heappush
import math


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        self.vertices[vertex1][vertex2] = weight

    def dijkstra(self, start_vertex):
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[start_vertex] = 0

        paths = {vertex: [] for vertex in self.vertices}
        paths[start_vertex] = [start_vertex]

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heappush(priority_queue, (distance, neighbor))

        return distances, paths

    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += str(vertex) + ": "
            for neighbor, weight in self.vertices[vertex].items():
                result += "(" + str(neighbor) + ", " + str(weight) + ") "
            result += "\n"
        return result


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 2)

distances_from_A, paths_from_A = g.dijkstra('A')

for vertex in g.vertices:
    if vertex != 'A':
        print(f"Najkrótsza odległość od 'A' do '{vertex}': {distances_from_A[vertex]}")
        print(f"Najkrótsza ścieżka od 'A' do '{vertex}': {' -> '.join(paths_from_A[vertex])}")
        print()