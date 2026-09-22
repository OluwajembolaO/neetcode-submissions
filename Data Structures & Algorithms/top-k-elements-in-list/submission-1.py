
class Solution:
    

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for num in nums:
            if num not in count: 
                count[num] = 1
            else:
                count[num] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for key in count:
            bucket[count[key]].append(key)

        for f in range(len(bucket) - 1, 0, -1):
            for num in bucket[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        
            
        