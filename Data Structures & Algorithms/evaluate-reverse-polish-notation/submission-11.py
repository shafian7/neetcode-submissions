class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']

        for t in tokens:
            if t in OPERATORS:
                if t == "+":
                    stack.append(stack.pop() + stack.pop())
                elif t == "-":
                    stack.append(-stack.pop() + stack.pop())
                elif t == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    denom = stack.pop()
                    stack.append(int(stack.pop() / denom))
            else:
                stack.append(int(t))
        
        return stack[0]
            