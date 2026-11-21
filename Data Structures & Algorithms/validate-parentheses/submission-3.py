class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            "{" : "}",
            "(" : ")",
            "[" : "]",
        }
        myStack = []
        for c in s:
            if c not in myDict:
                if not myStack or myDict[myStack[-1]] != c:
                    return False
                myStack.pop()
            else:
                myStack.append(c)
        return len(myStack) == 0
