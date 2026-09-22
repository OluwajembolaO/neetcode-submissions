class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myDictonary = {}
        for i in s:
            if i not in myDictonary:
                myDictonary[i] = 1
            else:
                myDictonary[i] += 1

        for j in t:
            if j not in myDictonary:
                return False
            else:
                myDictonary[j] -= 1
        for value in myDictonary.values():
            if value != 0:
                return False
        return True
        