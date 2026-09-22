class Solution:
    def romanToInt(self, s: str) -> int:
        myHash = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == "I" and s[i+1] == "V":
                print("IV")
                ans += 4
                i += 2
            elif s[i] == "I" and s[i+1] == "X":
                print("IX")
                ans += 9
                i += 2
            elif s[i] == "X" and s[i+1] == "L":
                print("XL")
                ans += 40
                i+=2 
            elif s[i] == "X" and s[i+1] == "C":
                print("XC")
                ans += 90
                i +=2 
            elif s[i] == "C" and s[i+1] == "D":
                print("CD")
                ans += 400
                i += 2
            elif s[i] == "C" and s[i+1] == "M":
                print("CM")
                ans += 900
                i += 2
            else:
                ans += (myHash[s[i]])
                i += 1

        if i == len(s) - 1:
            ans += myHash[s[i]]
        return ans