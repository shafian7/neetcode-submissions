class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tLength = len(temperatures)
        result = [0] * tLength

        for i in range(tLength - 2, -1, -1):
            j = 1
            while i + j < tLength:
                if temperatures[i + j] > temperatures[i]:
                    break
                else:
                    if result[i + j] == 0:
                        j = 0
                        break
                    else:
                        j += result[i + j]
            result[i] = j
        
        return result
                

    
                