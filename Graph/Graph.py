from __future__ import annotations
from typing import List

from collections import defaultdict

class Edge:
    def __init__(self, source, dest) -> None:
        self.source = source
        self.dest = dest

class WeightedEdge:
    def __init__(self, source, dest, cost) -> None:
        self.source = source
        self.dest = dest
        self.cost = cost

class Graph:
    def __init__(self, numOfNodes : int, edges : List[List[int]]) -> None:
        self.numOfNodes = numOfNodes
        self.edges = []
        self.adjList =  defaultdict(list)
        for source, dest in edges:
            self.adjList[source].append(dest)
            self.edges.append(Edge(source, dest))
        
class WeightedGraph:
    def __init__(self, numOfNodes : int, edges : List[List[int]]) -> None:
        self.numOfNodes = numOfNodes
        self.edges = []
        self.adjList = defaultdict(list)
        for source, dest, cost in edges:
            self.adjList[source].append([cost, dest])
            self.edges.append(WeightedEdge(source, dest, cost))