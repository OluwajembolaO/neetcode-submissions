class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        myArr = nums[:]
        for i in nums:
            myArr.append(i)
        return myArr

        