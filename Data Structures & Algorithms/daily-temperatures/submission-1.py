class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = []

        stack.append((0, temperatures[0]))

        for i in range(1, len(temperatures)):
            currTemp = temperatures[i]
            while stack and stack[len(stack) - 1][1] < currTemp:
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append((i, currTemp))
        

        return res
