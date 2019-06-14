class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def strtoInt(s):
            if s == "I":
                return 1
            elif s == "V":
                return 5
            elif s == "X":
                return 10
            elif s == "L":
                return 50
            elif s == "C":
                return 100
            elif s == "D":
                return 500
            elif s == "M":
                return 1000

        if len(s) == 1:
            return strtoInt(s)
        else:
            sum = 0
            # for i in range(0,len(s)):
            i = 0
            while i < len(s):
                if i + 1 < len(s):
                    left = strtoInt(s[i])
                    right = strtoInt(s[i + 1])
                    # print("left=",left,"right=",right)
                    if left >= right:
                        sum += left
                    else:
                        sum += (right - left)
                        i += 1
                    i += 1
                else:
                    if i < len(s):
                        sum += strtoInt(s[i])
                    break

        return sum