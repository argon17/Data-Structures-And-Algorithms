from __future__ import annotations
from typing import List

from Graph import Graph

class KahnsAlgorithm:
    def getTopologicalOrder(self, graph : Graph) -> List[int]:
        nodes, adjList = graph.numOfNodes, graph.adjList
        dependency = [0] * nodes
        for node in range(nodes):
            for adjNode in adjList[node]:
                dependency[adjNode] += 1
        processingNodes, topologicalOrder = [], []
        for node in range(nodes):
            if dependency[node] == 0:
                processingNodes.append(node)
        while processingNodes:
            node = processingNodes.pop()
            topologicalOrder.append(node)
            for adjNode in adjList[node]:
                dependency[adjNode] -= 1
                if dependency[adjNode] == 0:
                    processingNodes.append(adjNode)
        return topologicalOrder
    
def main():
    numOfNodes = 5
    edges = [[0, 1], [2, 1], [3, 2], [2, 4]]
    graph = Graph(numOfNodes, edges)
    kahnsalgo = KahnsAlgorithm()
    ans = kahnsalgo.getTopologicalOrder(graph)
    print(ans)
            
if __name__ == '__main__':
    main()
    