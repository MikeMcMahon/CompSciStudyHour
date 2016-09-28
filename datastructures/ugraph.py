"""

MikeMcMahon - 9/26/2016

"""
from typing import Tuple, Dict


class UGraph(object):
    def __init__(self):
        self.graph = {}

    def neighbors(self, vertex: str):
        if vertex not in self.graph:
            raise KeyError("vertex -{}- does not exist within this graph".format(vertex))

        return len(self.graph.get(vertex, set()))

    def add_vertex(self, vertex: str):
        if vertex not in self.graph:
            self.graph[vertex] = set() # No adges have been associated with this vertex

    def add_edge(self, x: str, y: str):
            self._add_edge(x, y)
            self._add_edge(y, x)

    def _add_edge(self, x, y):
            if x in self.graph:
                self.graph[x].add(y)
            else:
                self.graph[x] = set()
                self.graph[x].add(y)

    def remove_vertex(self, vertex: str):
        self.graph.pop(vertex, None)
        for x in self.graph.keys():
            if vertex in self.graph[x]:
                self.graph[x].remove(vertex)

    def remove_edge(self, x: str, y: str):
        if x in self.graph:
            self.graph[x].remove(y)
        if y in self.graph:
            self.graph[y].remove(x)

    def generate_incidence(self):
        vertices = sorted(self.graph.keys())
        y_v = len(vertices)

        distinct_edges = set()
        for v in vertices:
            edges = self.graph[v]
            edges = [tuple(sorted([v, e])) for e in edges]
            for e in edges:
                distinct_edges.add(e)

        x_e = len(distinct_edges)

        incidence = [[False for _ in range(len(distinct_edges))] for _ in range(len(vertices))]
        distinct_edges = sorted(distinct_edges)
        y, x = 0, 0
        for v in vertices:
            for edge in distinct_edges:
                incidence[y][x] = True if v in edge else False
                x += 1
            x = 0
            y += 1

        return incidence





def main():
    graph = UGraph()
    graph.add_vertex('e')
    graph.add_vertex('g')
    graph.add_edge('a', 'b')
    graph.add_edge('b', 'c')
    graph.add_edge('a', 'd')
    graph.add_edge('e', 'g')

    print()
    for r in graph.generate_incidence():
        incidence = ""
        for v in r:
            incidence += "1 " if v else "0 "
        print(incidence)

    print()

    print('A has {} neighbors.'.format(graph.neighbors('a')))
    print('B has {} neighbors.'.format(graph.neighbors('b')))
    print('G has {} neighbors.'.format(graph.neighbors('g')))

    graph.remove_vertex('a')
    graph.remove_edge('e', 'g')

    try:
        print('A has {} neighbors.'.format(graph.neighbors('a')))
    except KeyError as ex:
        print(ex)

    print('B has {} neighbors.'.format(graph.neighbors('b')))
    print('G has {} neighbors.'.format(graph.neighbors('g')))

    return


if __name__ == "__main__":
    main()
