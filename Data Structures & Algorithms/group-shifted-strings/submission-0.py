def leftShift(string):
    arr = []
    
    for i in range(1, 26):
        s = ""
        for c in string:
            shifted = (ord(c) - ord('a') - i) % 26
            s += chr(shifted + ord('a'))
        arr.append(s)
    arr.append(string)
    return arr

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        print(strings)
        ans = []
        myHash = {}
        for s in strings:
            myTup = tuple(sorted(leftShift(s)))
            if myTup not in myHash:
                myHash[myTup] = [s]
            else:
                myHash[myTup].append(s)
        for tup in myHash:
            ans.append(myHash[tup])
        print(ans)
        return ans

    
        














