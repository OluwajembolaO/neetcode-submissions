from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []
        order = []

        for i in range(len(nums)):
            order.append([])
        for key in freq:
            order[freq[key] - 1].append(key)
        
        for row in order[::-1]:
            for num in row[::-1]:
                if k == 0:
                    return ans 
                ans.append(num)
                k -= 1
        return ans