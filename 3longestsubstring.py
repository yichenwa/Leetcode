class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = []
        largest = 0
        for c in s:
            if c in substr:
                c_index = substr.index(c)
                if len(substr) > largest:
                    largest = len(substr)
                substr = substr[c_index + 1:len(substr)]
                substr.append(c)

            else:
                substr.append(c)
                if len(substr) >= largest:
                    largest = len(substr)
            # print(substr)
        return (largest)

