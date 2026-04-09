class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                current_heights = heights[left]
                max_area = max(max_area, width * current_heights)
                left += 1
            else:
                current_heights = heights[right]
                max_area = max(max_area, width * current_heights)
                right -= 1
        return max_area