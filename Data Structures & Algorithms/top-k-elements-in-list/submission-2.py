class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1     
        # DOESNT CREATE INDEPENDENT LIST 
        myList = []
        for i in range(len(nums)+1):
            myList.append([])
        
        for key in hashmap:
            #print("Map: ", hashmap[key])
            
            myList[hashmap[key]].append(key)
            #print("List: ", myList)
        
        ans = []
        i = -1
        while k > 0:
            if len(myList[i]) != 0:

                for j in range(len(myList[i])):
                    ans.append(myList[i][j])
                    k -= 1    
            i -= 1
        return ans

