class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right: #因为我们要找具体的数字，不能漏掉它，所以要写等于
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[right]:
                if nums[left] <= target <nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left += 1
                else:
                    right = mid -1
        return -1

