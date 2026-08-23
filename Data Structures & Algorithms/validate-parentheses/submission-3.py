class Solution:
    def isValid(self, s: str) -> bool:
        
        p = {']':'[', '}':'{', ')':'('}

        stack = []

        for c in s:
            if c in set(p.values()):
                stack.append(c)
            elif c in set(p.keys()):
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != p[c]:
                    return False
        
        return len(stack) == 0
                