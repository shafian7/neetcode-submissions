from math import ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for curr in tokens:
            if curr in operators:
                if curr == "+":
                    stack.append(int(stack.pop() + stack.pop()))
                if curr == "-":
                    stack.append(int(-(stack.pop() - stack.pop())))
                if curr == "*":
                    stack.append(int(stack.pop() * stack.pop()))
                if curr == "/":
                    denom = stack.pop()
                    stack.append(int(stack.pop() / denom))
            else:
                stack.append(int(curr))
        
        return ceil(stack[0])