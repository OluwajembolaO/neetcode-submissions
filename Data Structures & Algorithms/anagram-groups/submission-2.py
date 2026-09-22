class Solution:
    def tupleMaker(self, word: str) -> tuple:
        arr = [0] * 26
        for c in word:
            arr[ord(c )- ord("a")] += 1
        arr = tuple(arr)
        return arr
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for word in strs:
            letterFreq = self.tupleMaker(word)
            if letterFreq not in myDict:
                myDict[letterFreq] = [word]
            else:
                myDict[letterFreq].append(word)
        return list(myDict.values())
            