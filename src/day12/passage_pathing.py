import os


class Graph:
    def __init__(self, input) -> None:
        self.nodes = dict()
        for i in input:
            if i[0] not in self.nodes:
                n0 = Node(i[0])
                self.nodes[i[0]] = n0
            else:
                n0 = self.nodes[i[0]]
            if i[1] not in self.nodes:
                n1 = Node(i[1])
                self.nodes[i[1]] = n1
            else:
                n1 = self.nodes[i[1]]
            n0.add_connection(n1)
            n1.add_connection(n0)

        self.start = self.nodes['start']
        self.end = self.nodes['end']

    def count_paths(self, small_revisit_allowed=False) -> None:
        self.n_paths = 0

        def mod_dfs(node, visited, small_revisit_allowed):
            if node == self.end:
                self.n_paths += 1
                return
            elif node.is_small():
                if node in visited:
                    if small_revisit_allowed and node == self.start:
                        for conn in node.connections:
                            mod_dfs(conn, visited, False)
                    else:
                        return
                else:
                    for conn in node.connections:
                        mod_dfs(conn, visited | {node}, small_revisit_allowed)
            else:
                for conn in node.connections:
                    mod_dfs(conn, visited | {node}, small_revisit_allowed)

        visited = set()
        mod_dfs(self.start, visited, small_revisit_allowed)
        return self.n_paths


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.connections = set()

    def add_connection(self, connection) -> None:
        if connection not in self.connections:
            self.connections.add(connection)

    def is_small(self) -> bool:
        return str.islower(self.value)


if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(filename) as f:
        input = [l.strip().split('-') for l in f.readlines()]

    g = Graph(input)
    p1_sol = g.count_paths(small_revisit_allowed=False)
    print("Part 1 Solution:", p1_sol)

    p2_sol = g.count_paths(small_revisit_allowed=True)
    print("Part 2 Solution:", p2_sol)
