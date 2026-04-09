class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #用map建立映射关系
        preMap ={i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visitSet = set()

        def dfs(crs):
            #base 1
            if crs in visitSet:
                return False
            #base 2
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            #撤销标记（因为这个crs)没问题了
            visitSet.remove(crs)
            preMap[crs] = [] #可以直接在base2返回ture
            return True
        #正式的去跑dfs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True