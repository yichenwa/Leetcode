class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        dis = 2 * (numRows - 1)
        if len(s) <= numRows or dis == 0:
            return s

        for r in range(0, numRows):

            if r == 0 or r == numRows - 1:
                i = 0
                while (r + i * dis < len(s)):
                    result += s[r + i * dis]
                    # print(result)
                    i += 1

            else:
                disr = 2 * r
                disl = dis - disr
                ind = r
                i = 0
                while (ind < len(s)):
                    result += s[ind]
                    # print(result)
                    i += 1
                    if (i % 2 == 1):
                        ind += disl
                    else:
                        ind += disr

        return result