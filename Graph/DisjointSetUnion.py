class DisjointSetUnion:
    def __init__(self, numOfNodes : int) -> None:
        self.parent = [node for node in range(numOfNodes)]
        
    def find(self, n : int) -> int:
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
            
    def union(self, n1 : int, n2 : int) -> None:
        root1, root2 = self.find(n1), self.find(n2)
        if root1 != root2:
            self.parent[root1] = root2