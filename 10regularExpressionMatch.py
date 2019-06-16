class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #. any char    .* any combine   n==n n* nnnnn or 0
        #si pi
        for pi in range(0,len(p)):
            