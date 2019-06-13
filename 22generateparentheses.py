class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def pps(n):
            if n == 0:
                return []
            elif n == 1:
                return ["()"]
            elif n >= 2:

                last_l = pps(n - 1)
                l = []
                for sub_l in last_l:
                    for i in range(0, len(sub_l) - 1):
                        if sub_l[i] == "(" and sub_l[i + 1] == ")":
                            s1 = sub_l
                            rs1 = s1[0:i + 1] + "()" + s1[i + 1:len(sub_l)]
                            s2 = sub_l
                            rs2 = s2[0:i + 2] + "()" + s2[i + 2:len(sub_l)]
                            l.append(rs1)
                            l.append(rs2)
                l2 = list(set(l))
                return l2

        return pps(n)