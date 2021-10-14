import heapq
from collections import deque

from typing import List


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    # self.adj_list = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['B', 'A'], 'D': ['B']}

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph or nothing if vertex exists.
        """
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        (this method also sorts the edge list)
        """
        if u == v:
            return
        if u not in self.adj_list:
            self.adj_list[u] = [v]
        if v not in self.adj_list:
            self.adj_list[v] = [u]
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if u == v:
            return
        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)
            self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v in self.adj_list:
            del self.adj_list[v]
            for item in self.adj_list:
                if v in self.adj_list[item]:
                    self.adj_list[item].remove(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        return list(self.adj_list.keys())

    def get_edges(self) -> [tuple]:
        """
        Return list of edges in the graph (any order) with each vertex's values as tuples
        """
        all_edges = []
        for key in self.adj_list:
            for value in self.adj_list[key]:
                if (value, key) not in all_edges:
                    all_edges.append((key, value))
        # remove duplicates ie., [(a, b), (b, a)] ==> [(a, b)]
        return all_edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        if len(path) == 0:
            return True
        if len(path) == 1:
            return path[0] in self.adj_list.keys()
        list_of_truth = []
        for c, n in zip(path, path[1:]):
            if c in self.adj_list and n in self.adj_list[c]:
                list_of_truth.append(True)
            else:
                return False
        return False not in list_of_truth

    # --------------------------------------------------------------------------------------------------------------------------------------------------------
    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order.
        """
        arr = []
        visited = []
        if v_end:
            return arr.append(v_end)

        keys = []

        for vertex in self.adj_list.keys():
            keys.append(vertex)

        if v_start not in keys:
            return []


        self.adj_list[v_start].sort()
        self.dfs_helper(v_start, v_end, visited)

        return visited


    def dfs_helper(self, v_start, v_end, visited):
        if not v_start:
            return
        if v_start in visited:
            return

        visited.append(v_start)

        if v_start == v_end:
            return

        for value in self.adj_list[v_start]:
            self.adj_list[value].sort()
            self.dfs_helper(value, v_end, visited)


    # --------------------------------------------------------------------------------------------------------------------------------------------------------

    def bfs(self, v_start, v_end=None):
        visited = [v_start]
        queue = deque([v_start])

        while queue:
            if v_start == v_end:
                visited.append(v_end)
                return
            # Dequeue a vertex from queue
            vertex = queue.pop()

            # If not visited, mark it as visited, and
            # enqueue it
            for neighbour in reversed(self.adj_list[vertex]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited


    # --------------------------------------------------------------------------------------------------------------------------------------------------------

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        visited = set()
        cc = []
        for v in self.adj_list.keys():
            if v not in visited:
                tp = []
                cc.append(self.dfs_helper(v, visited, tp))
        return len(cc)


    # --------------------------------------------------------------------------------------------------------------------------------------------------------
    def has_cycle_util(self, v, visited, p):
        visited.add(v)
        for u in self.adj_list[v]:
            if u not in visited:
                has_cycle = self.has_cycle_util(u, visited, v)
                if has_cycle:
                    return True
            elif p != u:
                return True
        return False


    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        visited = set()
        for v in self.adj_list.keys():
            if v not in visited:
                has_cycle = self.has_cycle_util(v, visited, '0')
                if has_cycle:
                    return True
        return False


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)

    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)

    # g.add_vertex('A')
    # print(g)

    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)

    # #
    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)

    # print("\nPDF - method get_vertices() / get_edges() example 1")
    # print("---------------------------------------------------")
    # g = UndirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    # print(g.get_edges(), g.get_vertices(), sep='\n')

    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # # test_cases = ['ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # test_cases = ['ECABDCBE']
    # for path in test_cases:
    #     print(list(path), g.is_valid_path(list(path)))

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')
    #
    #
    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    #
    # #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
