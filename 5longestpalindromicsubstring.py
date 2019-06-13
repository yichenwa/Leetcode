class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        outstr=""
        rs=s[::-1]
        for i in range(0,len(s)):
            if (len(s)-i-1)<len(result):
                break
            outstr=""
            for j in range(i,len(s)):
                outstr+=s[j]
                if outstr==outstr[::-1]:
                    if len(outstr)>len(result):
                        result=outstr
        return result          