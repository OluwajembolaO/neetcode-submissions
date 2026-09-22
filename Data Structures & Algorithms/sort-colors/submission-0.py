class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*3
        for val in nums:
            bucket[val] += 1

        j = 0 #Putting input of the array
        for i in range(len(bucket)): #Gets the index of bucket
            for k in range(bucket[i]): #Gets the amount of times it takes to loop 
                nums[j] = i
                j += 1
        return nums

            
        