class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses = {'(':')', "{": "}", "[":"]"}
        pKeys = set(parentheses.keys())
        pVals = set(parentheses.values())
        for char in s:
            if char in pKeys:
                stack.append(char)
            elif char in pVals:
                if stack == [] or char != parentheses[stack.pop()]:
                    return False
        
        return not stack
