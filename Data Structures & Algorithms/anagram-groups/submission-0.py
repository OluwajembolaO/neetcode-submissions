
class Solution:
    def tupleMachine(self, strs ):
        myArr = [0] * 26
        for s in strs:
            # ord('a') -> int (97)
            myArr[ord(s) - 97] += 1
        myArr = tuple(myArr)
        return myArr

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            val = self.tupleMachine(s)
            if val not in hashmap:
                hashmap[val] = [s]
            else:
                hashmap[val].append(s)
        return list(hashmap.values())
        