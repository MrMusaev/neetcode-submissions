class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
                
        adjList = defaultdict(list)
        for node, neighbor in edges:
            adjList[node].append(neighbor)
            adjList[neighbor].append(node)
        
        def dfs(nodeVal, visited, prev):
            if nodeVal in visited:
                return False
            
            noCycle = True
            visited.add(nodeVal)
            for neighbor in adjList[nodeVal]:
                if neighbor == prev:
                    continue
                noCycle = noCycle and dfs(neighbor, visited, nodeVal)

            return noCycle

        visited = set()
        noCycle = dfs(0, visited, -1)

        if not noCycle:
            return False
        
        return len(visited) == n