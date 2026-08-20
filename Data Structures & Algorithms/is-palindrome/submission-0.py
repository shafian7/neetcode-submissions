class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        comparator = ""

        for char in s:
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                comparator += char.lower()
            if '0' <= char <= '9':
                comparator += char
        
        return comparator == comparator[::-1]
