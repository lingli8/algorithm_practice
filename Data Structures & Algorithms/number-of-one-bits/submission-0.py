class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            count += (n&1) # n&1 记住：对最后一位判断，都1则1，否则为0
            n = n >> 1
        return count
    