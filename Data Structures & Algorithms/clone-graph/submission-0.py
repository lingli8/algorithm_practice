"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            copy_node = Node(node.val)
            old_to_new[node] = copy_node
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                copy_node.neighbors.append(cloned_neighbor)
            return copy_node
        return dfs(node)