class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        charList = []
        result = 0
        for ch in s:
            if (ch in charList):
                charList = charList[charList.index(ch) + 1:]
            
            charList.append(ch)
            result = max(result, len(charList))
        
        return result
