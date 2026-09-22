class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myHash = {}
        for num in nums:
            if num not in myHash:
                myHash[num] = 1
            else:
                myHash[num] += 1
        for key in myHash:
            if max(len(nums)/2, myHash[key]) == myHash[key]:
                return key
            
        