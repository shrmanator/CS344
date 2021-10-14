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
        This method adds a new edge to the graph,
        connecting the two vertices with the provided indices *src* and *dst*.
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
        represents a valid path in the graph.
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
        if v_start < 0 or v_start >= self.v_count:
            return []

        visited = [False for i in range(self.v_count)]

        # Create a stack for DFS
        stack = []

        #
        dfs_list = []

        # Push the current source node.
        stack.append(v_start)

        while len(stack):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                dfs_list.append(s)
                visited[s] = True

            if s == v_end:
                return dfs_list

            # Iterate on vertices in reveres order so that on top side of the stack
            # we have the correct element in the order and if the node is adjacent then push
            # that onto stack
            for node in reversed(range(self.v_count)):
                if not visited[node] and self.adj_matrix[s][node] > 0:
                    stack.append(node)

        return dfs_list

    def bfs(self, v_start, v_end=None) -> []:
        # first check if the v_start is a valid node
        # if it is not a valid node then simply return an empty list
        if v_start < 0 or v_start >= self.v_count:
            return []

        # create a visited list and mark all nodes as unvidisted
        visited = [False] * self.v_count

        # this list will store our answer, that is in the order bfs was performed
        bfs_list = []

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        visited[v_start] = True
        queue.append(v_start)

        while queue:

            # The front of the queue is the next node to be visited
            u = queue.pop(0)

            # add the current node to bfs list
            bfs_list.append(u)

            # if we have reached the end node then return the bfs list until now
            if u == v_end:
                return bfs_list

            # now iterate on all adjacent nodes of current nodes and
            #  if that is still unvivited then enque it
            for i in range(self.v_count):
                if not visited[i] and self.adj_matrix[u][i] > 0:
                    queue.append(i)
                    visited[i] = True
        return bfs_list

    def get_cycle(self, u, visited, rec_stack):
        # since we have visited u node mark this vivisted and this node to recusion stack
        visited[u] = True
        rec_stack[u] = True

        # now find the edges to node u and if we find that that is still unvivted then visit that
        # in case we find that the vertex is in the recusion stack that means that graph has cycle
        # hence return true in that case
        for v in range(self.v_count):
            if self.adj_matrix[u][v] == 0:
                continue

            if not visited[v]:
                if self.get_cycle(v, visited, rec_stack):
                    return True
            elif rec_stack[v]:
                return True

        # once done mark node u as not on the stack
        rec_stack[u] = False
        return False

    def has_cycle(self):
        visited = [False] * self.v_count
        rec_stack = [False] * self.v_count
        for node in range(self.v_count):
            if not visited[node]:
                if self.get_cycle(node, visited, rec_stack):
                    return True
        return False

    def get_least_distance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = 2147483646
        min_index = 0
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.v_count):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src: int) -> []:
        dist = [2147483646] * self.v_count
        dist[src] = 0
        sptSet = [False] * self.v_count

        for i in range(self.v_count):
            # first get the node which has smallest dist in sptSet
            u = self.get_least_distance(dist, sptSet)
            # now since that node is taken into sptSet mark it true
            sptSet[u] = True

            # not iteraete on vertices and if we can chane the distance of adjacent vertexex then do it
            for v in range(self.v_count):
                if self.adj_matrix[u][v] > 0 and sptSet[v] == False and dist[v] > (dist[u] + self.adj_matrix[u][v]):
                    dist[v] = dist[u] + self.adj_matrix[u][v]

        for i in range(len(dist)):
            if dist[i] == 2147483646:
                dist[i] = float('inf')
        return dist


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
