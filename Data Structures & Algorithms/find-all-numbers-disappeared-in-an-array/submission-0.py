class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        for i in range(1, length + 1):
            if i not in set(nums):
                ans.append(i)
        return ans
        