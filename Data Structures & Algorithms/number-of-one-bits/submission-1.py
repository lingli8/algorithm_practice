class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n&(n-1) #每运行一次则消除一个1 —— 效率更高
            count += 1
        return count