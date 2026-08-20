class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []

        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                result[anagram_dict[sorted_word]].append(word)
            else:
                anagram_dict[sorted_word] = len(result) 
                result.append([word])


        return result