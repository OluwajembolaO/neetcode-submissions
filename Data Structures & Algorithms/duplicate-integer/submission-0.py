class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberTracker = {}
        for num in nums:
            if num in numberTracker:
                return True
            else:
                numberTracker[num] = 1
        return False 
        