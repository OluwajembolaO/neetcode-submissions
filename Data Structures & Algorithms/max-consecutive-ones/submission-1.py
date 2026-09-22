class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        cnt = 0
        for n in nums:
            if n == 0:
                maxi = max(maxi, cnt)
                cnt = 0
            else:
                cnt += 1
        return max(maxi,cnt)   
   
                
        