class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for currString in strs:
            result += f"{str(len(currString))}*{currString}"

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        currIndex = 0
        strLength = ""
        while currIndex < len(s):
            while s[currIndex] != "*":
                strLength += s[currIndex]
                currIndex += 1
            currIndex += 1
            strLength = int(strLength)
            currStr = s[currIndex:currIndex + strLength]
            currIndex += strLength
            result.append(currStr)
            strLength = ""
        
        return result

        