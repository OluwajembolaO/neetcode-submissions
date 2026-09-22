
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHash = set()
        for n in nums:
            if n not in myHash:
                myHash.add(n)
            else:
                return True
        return False