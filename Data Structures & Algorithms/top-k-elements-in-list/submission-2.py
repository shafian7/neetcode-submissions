import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberDict = defaultdict(int)

        for num in nums:
            numberDict[num] += 1
        
        result = []

        sortedArray = sorted(numberDict.items(), key= operator.itemgetter(1), reverse=True)

        for i in range(len(sortedArray)):
            if (i < k):
                if (not sortedArray[i][0] in result):
                    result.append(sortedArray[i][0])

        
                
        return result