"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfsClone(self, node: Optional['Node'], visited_map: dict) -> Optional['Node']:
        if not node:
            return None
        
        # 1. Check if node is already in visited_map
        if node.val in visited_map:
            return visited_map[node.val]

        # 2. Create a new node to clone
        # update visited_map
        cloned_node = Node(node.val)
        visited_map[node.val] = cloned_node

        # 3. Iterate through node neighbors and call dfs 
        # append returned result to cloned node
        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.dfsClone(neighbor, visited_map))
        
        # 4. Return the cloned node
        return cloned_node


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_map = {}
        return self.dfsClone(node, visited_map)