class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        #建立联系
        adj ={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        #定义是否是孤立的点
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n