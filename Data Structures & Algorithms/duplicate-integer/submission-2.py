class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set(nums)
        if len(list_set) != len(nums):
            return True
        return False
       