class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = []
        for num in nums :
            if num in number:
                return True
            number.append(num)
        return False
       
        