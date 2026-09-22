class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodupe = []
        for x in nums:
            if x not in nodupe:
                nodupe.append(x)
            else:
                return True
        return False
            
        