class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        output = []
        visited = set() #永久名单：记录“已经修完并加入output”的课
        cycle  = set() #临时名单：记录“当前递归路径”上的课 (防环)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output

