#!env python3
# Finding the Longest Palindromic Substring

import timer_wraps

class Solution:

    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        m = int(length/2)

        for i in range(0, m):
            if s[i] != s[length - i - 1]:
                return False
        return True

    # return the length of expanded string
    def expandAroundCenter(self, s: str, length: int, left: int, right: int) -> int:
        L = left
        R = right

        while L >= 0 and R < length and s[L] == s[R]:
            L = L - 1
            R = R + 1

        R = R - 1
        L = L + 1

        return R - L + 1

    @timer_wraps.measure_time
    def longestPalindromeExpand(self, s: str) -> str:
        length = len(s)
        start = 0
        end = 0

        # i is the positon of center
        i = 0
        while i < length:
            len1 = self.expandAroundCenter(s, length, i, i)
            len2 = self.expandAroundCenter(s, length, i, i + 1)
            maxLen = max(len1, len2)

            if maxLen > (end - start + 1):
                start = i - int((maxLen - 1)/2)
                end = i + int((maxLen)/2)
            i = i + 1

        return s[start: end + 1]

    @timer_wraps.measure_time
    def longestPalindromeDP(self, s: str) -> str:
        length = len(s)
        result = 1

        start = 0
        table = [[False for x in range(length)] for y in range(length)]
        for i in range(length):
            table[i][i] = True

        i = 0
        while i < length - 1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                result = 2
            i = i + 1

        # n is the length of substring
        n = 3
        while n <= length: 
            i = 0
            while i < (length - n + 1):
                j = i + n - 1

                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True

                    if n > result:
                        start = i
                        result = n

                i = i + 1
            n = n + 1
        print(s[start: start + result])
        return result


    @timer_wraps.measure_time
    def longestPalindromeBruteForce(self, s: str) -> str:
        length = len(s)
        result = 0

        for i in range(length):
            for j in range(i + 1, length + 1):
                if self.isPalindrome(s[i:j]):
                    result = max(j - i, result)

        return result

    def getModifiedString(self, s: str) -> str:
        modifiedString = '#'
        length = len(s)

        i = 0
        while i < length:
            modifiedString = modifiedString + s[i]
            modifiedString = modifiedString + '#'
            i = i + 1

        return modifiedString

    @timer_wraps.measure_time
    def longestPalindromeManacher(self, s: str) -> str:
        modifiedString = self.getModifiedString(s)
        print(modifiedString)
        length = len(s) * 2 + 1

        c = 0 # store the current longest palindrome substring
        r = 0 # store the right boundary of current longest palindrome substring

        P = [ 0 for x in range(length)]
        maxLen = 0
        # the center of longest palindrome substring
        start = 0
        
        i = 0
        while i < length:

            # mirror i = C - (i - C) = 2C - i
            mirror_i = 2 * c - i

            # if i is under boundary
            # if the mirror_i - P[mirror_i] is beyond the left boundary,
            # the minimum P is r - i
            if i < r:
                P[i] = min(r - i, P[mirror_i])

            # expand the string at i
            x = i - (P[i] + 1)
            y = i + (P[i] + 1)
            while x >= 0 and y < length and modifiedString[x] == modifiedString[y]:
                x = x - 1
                y = y + 1
                P[i] = P[i] + 1

            if i + P[i] > r:
                c = i
                r = i + P[i]

                if P[i] > maxLen:
                    maxLen = P[i]
                    start = c - P[c]

            i = i + 1

        i = int(start/2)
        return s[i: i + maxLen]

if __name__ == "__main__":
    s = "babadaadabeeefaefoijaefioe"
    solution = Solution()
    print(solution.longestPalindromeBruteForce(s))
    print(solution.longestPalindromeDP(s))
    print(solution.longestPalindromeExpand(s))
    print(solution.longestPalindromeManacher(s))
    #print(solution.isPalindrome('aba'))
    #print(solution.isPalindrome('ab'))
