class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            if token == "+":
                total = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            if token == "-":
                diff = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(diff)
            if token == "*":
                prod = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(prod)
            if token == "/":
                quot = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(quot)
        return stack[0]
            

        