class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            hours = 0
            mid_speed = (left + right) // 2
            for p in piles:
                hours += (mid_speed + p - 1) // mid_speed
            if hours <= h:
                res = mid_speed
                right = mid_speed -1
            else:
                left = mid_speed + 1
        return res