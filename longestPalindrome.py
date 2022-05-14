class Solution:    
    
    def isSubPalindrome(self, subString: str) -> str:
        if len(subString) == 1: return True
        if len(subString) == 2 and subString[0] == subString[1]: return True
        rev = subString[::-1]
        return subString == rev

    def longestPalindrome(self, s: str) -> str:
        sLength = len(s)
        if sLength == 0: return 0
        if sLength == 1: return s
        if sLength == 2 and s[0] != s[1]: return s[0]

        left, right = 0, sLength - 1
        longestPal = ''

        while left <= right:
            r = right
            isSubPal = False
            while isSubPal == False and r >= left:
                if s[left] == s[r]:
                    newString = s[left:r+1]
                    isSubPal = self.isSubPalindrome(newString)
                    if isSubPal == True and len(longestPal) < len(newString):
                        longestPal = newString
                r -= 1
            left += 1
        return longestPal