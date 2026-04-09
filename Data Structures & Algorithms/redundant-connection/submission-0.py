class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # len(edges) 就是 N，因为树是 N-1 条边，多加一条就是 N 条
        parent = [i for i in range(n+1)] #生成：parent = [0, 1, 2, 3, 4]，每个人的老大一开始都是自己
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) #找parent的parent
            return parent[node]
        #core code: how to find the extra one
        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return False
            parent[root2] = root1
            return True


        for u, v in edges:
            if not union(u,v):
                return [u,v]
        return []