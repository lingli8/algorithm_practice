# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_node):
            if not node:
                return 0
            res = 1 if node.val >= max_node else 0
            new_max = max(node.val, max_node)
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            return res
        return dfs(root, root.val)
        