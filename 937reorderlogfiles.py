class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l1 = []
        l2 = []
        i = 0
        for log in logs:
            sp_log = log.split()
            s = ""
            for j in range(1, len(sp_log)):
                s += sp_log[j]
                if s.isdigit() == False:
                    s += ' '

            if s.isdigit():
                # s+=sp_log[0]
                l2.append([s, i])
            else:
                s += sp_log[0]
                l1.append([s, i])
            i += 1

        # print(l1,l2)
        l1 = sorted(l1)
        # l2=sorted(l2)

        result = []
        for sub1 in l1:
            result.append(logs[sub1[1]])
        for sub2 in l2:
            result.append(logs[sub2[1]])

        return result