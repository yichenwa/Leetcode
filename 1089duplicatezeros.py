class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        len_a = len(arr)

        result = []
        for i in range(0, len_a):
            if arr[i] != 0 and len(result) < len_a:
                result.append(arr[i])
            elif arr[i] == 0 and len(result) < len_a:
                result.append(0)
                if len(result) < len_a:
                    result.append(0)
        for i in range(0, len_a):
            arr[i] = result[i]