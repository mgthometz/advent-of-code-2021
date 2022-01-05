import os
from queue import PriorityQueue

filename = os.path.join(os.path.dirname(__file__), "input.txt")
with open(filename) as f:
    input = [[int(i) for i in list(l.strip())] for l in f]


class Node:
    def __init__(self, risk: int) -> None:
        self.risk = risk
        self.neighbors = set()

    def add_neighbor(self, neighbor) -> None:
        self.neighbors.add(neighbor)


class Graph:
    def __init__(self, input: list[list]) -> None:
        self.nodes = dict()
        xmax = len(input[0]) - 1
        ymax = len(input) - 1
        for i in range(0, xmax + 1):
            for j in range(0, ymax + 1):
                risk = input[i][j]
                self.nodes[(i, j)] = Node(risk)
        for n in self.nodes.items():
            i, j = n[0][0], n[0][1]
            curr = n[1]
            if i > 0:
                curr.add_neighbor((i-1, j))
            if i < xmax:
                curr.add_neighbor((i+1, j))
            if j > 0:
                curr.add_neighbor((i, j-1))
            if j < ymax:
                curr.add_neighbor((i, j+1))

def Dijkstra(graph: Graph, source: tuple, target: tuple) -> None:
    dist = dict.fromkeys(graph.nodes.keys(), float('inf'))
    prev = dict.fromkeys(graph.nodes.keys(), None)
    dist[source] = 0
    unvisited = PriorityQueue()
    for n in graph.nodes:
        unvisited.put((dist[n], n))
    visited = set()
    while unvisited:
        current_dist, current_node = unvisited.get()
        if current_node == target:
            return dist[current_node]
        visited.add(current_node)
        for neighbor in graph.nodes[current_node].neighbors:
            if neighbor in visited:
                continue
            if graph.nodes[neighbor].risk + current_dist < dist[neighbor]:
                prev[neighbor] = current_node
                dist[neighbor] = graph.nodes[neighbor].risk + current_dist
                unvisited.put((dist[neighbor], neighbor))
    return -1


g = Graph(input)
source = g.nodes[(0, 0)]
target = g.nodes[(len(input) - 1, len(input[0]) - 1)]
print(Dijkstra(g, (0, 0), (len(input) - 1, len(input[0]) - 1)))


def extend_input(input):
    def extend_right(input):
        out = []
        for row in input:
            new = []
            for i in range(5):
                ext = [x+i if x+i < 10 else (x + i) % 10 + 1 for x in row]
                new.extend(ext)
            out.append(new)
        return out

    def extend_down(input):
        out = []
        for i in range(5):
            for row in input:
                new_row = [x+i if x+i < 10 else (x + i) % 10 + 1 for x in row]
                out.append(new_row)
        return out

    final = extend_down(extend_right(input))
    return final


extended_input = extend_input(input)
g2 = Graph(extended_input)
source = g2.nodes[(0,0)]
target = g2.nodes[(len(extended_input) - 1,len(extended_input[0]) - 1)]
print(Dijkstra(g2, (0,0), (len(extended_input) - 1,len(extended_input[0]) - 1)))