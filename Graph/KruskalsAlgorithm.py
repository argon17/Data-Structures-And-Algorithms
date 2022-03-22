from __future__ import annotations
from typing import List

from Graph import WeightedGraph, WeightedEdge
from DisjointSetUnion import DisjointSetUnion

class KruskalsAlgorithm:
    def findMinimumSpanningTree(self, graph : WeightedGraph) -> List[int, List[WeightedEdge]]:
        nodes, edges = graph.numOfNodes, graph.edges
        dsu = DisjointSetUnion(nodes)
        edges.sort(key = lambda edge : edge.cost)
        minimumCost, minimumSpanningTree = 0, []
        for edge in edges:
            if dsu.find(edge.source) != dsu.find(edge.dest):
                dsu.union(edge.source, edge.dest)
                minimumCost += edge.cost
                minimumSpanningTree.append(edge)
        return minimumCost, minimumSpanningTree


def main():
    numOfNodes = 5
    edges = [[0, 1, 4], [2, 4, 3], [1, 3, 5], [0, 3, 9], [2, 3, 7]]
    graph = WeightedGraph(numOfNodes, edges)
    kruskalalgo = KruskalsAlgorithm()
    minimumCost, minimumSpanningTree = kruskalalgo.findMinimumSpanningTree(graph)
    print(minimumCost)
    for edge in minimumSpanningTree:
        print(edge.source, edge.dest, edge.cost)

if __name__ == '__main__':
    main()
    