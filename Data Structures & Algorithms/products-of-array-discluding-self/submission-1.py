class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        preFix = [1] * length
        postFix = [1] * length
        for i in range(1,length):
            preFix[i] = preFix[i - 1] * nums[i - 1]
        for i in range((length -2), -1, -1):
            postFix[i] = postFix[i + 1] * nums[i + 1]
        for i in range(length):
            ans.append(preFix[i] * postFix[i])

        return ans
        