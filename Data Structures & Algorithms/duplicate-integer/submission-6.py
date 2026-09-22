from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHash = Counter(nums)
        for key in myHash:
            if myHash[key] > 1:
                return True
        return False