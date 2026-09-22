class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for val in nums:
            if val == 1:
                count += 1
            else:
                if count > maxi:
                    maxi = count
                count = 0
        
        if maxi > count:
            return maxi
        return count
                
        