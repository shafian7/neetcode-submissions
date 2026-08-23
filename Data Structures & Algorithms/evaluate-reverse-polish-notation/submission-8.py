from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for curr in tokens:
            if curr == "+":
                stack.append(stack.pop() + stack.pop())
            elif curr == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif curr == "*":
                stack.append(stack.pop() * stack.pop())
            elif curr == "/":
                denom = stack.pop()
                stack.append(int(stack.pop() / denom))
            else:
                stack.append(int(curr))
        
        return ceil(stack[0])