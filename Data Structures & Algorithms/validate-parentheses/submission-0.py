class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        myStack = []
        for char in s:
            if char in myDict:
                myStack.append(char)
            else:
                if len(myStack) == 0:
                    return False
                if myDict[myStack[-1]] != char:
                    return False
                else:
                    myStack.pop()
        if len(myStack) == 0:
            return True
        return False


        