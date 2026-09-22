class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for c in s:
            if c not in myDict:
                myDict[c] = 1
            else:
                myDict[c] += 1
        for c in t:
            if c not in myDict:
                return False
            else:
                myDict[c] -= 1

        for key in myDict:
            if myDict[key] != 0:
                return False
        return True