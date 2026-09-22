class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        ans = []
        for num in nums: 
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1
        freqTable = []
        for i in range(len(nums)):
            freqTable.append([])
        
        for key in myDict:
            freqTable[myDict[key]-1].append(key)
        for row in freqTable[::-1]:
            for num in row[::-1]:
                if (k == 0):
                    return ans
                ans.append(num)
                k -=1
        return ans
