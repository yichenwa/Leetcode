class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        class Solution(object):
            def myAtoi(self, str):
                """
                :type str: str
                :rtype: int
                """
                maxint = 2 ** 31 - 1
                minint = -1 * (2 ** 31)

                def check(test, i):
                    if (i == 0 and (test[i] == '+' or test[i] == '-')):
                        return True
                    else:
                        try:
                            int(test[i])
                            return True
                        except ValueError:
                            return False

                if len(str) == 0:
                    return 0
                else:
                    sub = str.split()
                    if len(sub) == 0:
                        return 0
                    else:
                        test = sub[0]
                        if len(test) == 0:
                            return 0
                        s = ""
                        for i in range(0, len(test)):
                            # print("check=",test[i],check(test,i))
                            if check(test, i):
                                s += test[i]
                            else:
                                # print s
                                break

                        try:
                            int(s)
                            if int(s) > maxint:
                                return maxint
                            elif int(s) < minint:
                                return minint
                            else:
                                return int(s)
                        except:
                            return 0



