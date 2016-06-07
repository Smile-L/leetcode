import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:return True
        s = s.lower()
        s = s.replace(' ', '')
        s = "".join([c for c in s if c not in string.punctuation])
        l = len(s)/2
        for i in range(l):
            if s[i]!=s[-i-1]:
                return False
        return True