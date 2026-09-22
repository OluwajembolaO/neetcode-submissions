class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stor = 0
        for i in range(len(digits)):
            stor += digits[i] * (10 **(len(digits) - i - 1))
        stor += 1
        ans = []
        while stor > 0:
            digit = stor % 10
            ans.append(digit)
            stor //=10
        return ans[::-1]
            
        