# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import heapq
from collections import deque

from typing import Tuple


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a vertex to graph and returns the number of vertices in the graph after the addition.
        """
        self.adj_matrix.append([])
        self.v_count += 1

        for i in range(self.v_count):
            self.adj_matrix[i] = [0 for each_vertex in range(self.v_count)]

        return len(self.adj_matrix)

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        scr --weight--> dst: where scr = source and dst = destination.

        This method adds a new edge to the graph,
        connecting the two vertices with the provided indices *src* and *dst*.

        Precondition: weight >= 0
        """
        matrix_size = len(self.adj_matrix)
        if (0 <= src < matrix_size
                and 0 <= dst < matrix_size
                and weight >= 0
                and src != dst):
            source_vertex = self.adj_matrix[src]
            source_vertex[dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between two vertices with provided indices.
        """
        matrix_size = len(self.adj_matrix)
        if (0 <= src < matrix_size
                and 0 <= dst < matrix_size
                and src != dst):
            source_vertex = self.adj_matrix[src]
            source_vertex[dst] = 0

    def get_vertices(self) -> [int]:
        """
        Returns a list of vertices of the graph.
        """
        return [vertex_name for vertex_name in range(self.v_count)]

    def get_edges(self) -> [Tuple[int]]:
        """
        Returns a list of edges in the graph.

        Format:
            Each edge is returned as a tuple of two incident vertex indices and weight.
             First element in the tuple refers to the source vertex.
              Second element in the tuple refers to the destination vertex.
               Third element in the tuple is the weight of the edge.
        """
        lst = []
        for vertex in self.get_vertices():
            edge_list = self.adj_matrix[vertex]
            for i in range(len(edge_list)):
                if edge_list[i] != 0:
                    tup = (vertex,)
                    tup += (i, edge_list[i])  # i = dst index and edge_list[i] = weight of edge
                    lst.append(tup)
        return lst

    def is_valid_path(self, path: [int]) -> bool:
        """
        Takes a list of vertex indices and returns True if the sequence of vertices
        represents a valid path in the graph (so one can travel from the first vertex
        in the list to the last vertex in the list, at each step traversing over an edge in the graph).

        Note: Empty paths are considered valid.
        """
        visited = []  # inserts True if a vertex gets visited.
        all_vertices = self.get_vertices()
        for current_vertex, next_vertex in zip(path, path[1:]):
            curr_edge_list = self.adj_matrix[current_vertex]
            if current_vertex in all_vertices and curr_edge_list[next_vertex] != 0:
                if self.adj_matrix[current_vertex] != 0:
                    visited.append(True)
            else:
                return False
        return False not in visited

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        # use a priority queue to order our search.
        pass


if __name__ == '__main__':
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    # #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)
    #
    #
    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)
    #
    #
    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
