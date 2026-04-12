class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #1/找快慢相遇点 2/抓fast回来到出发点，再同步进行走，最后相遇的点就return
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow