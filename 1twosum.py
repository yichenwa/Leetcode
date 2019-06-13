class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            num1=nums[i]
            num2 = target - num1
            newnums=nums[0:i]+nums[i+1:len(nums)]
            if num2 in newnums:
                return [nums.index(num1), newnums.index(num2)+1]
        return []

t=Solution()
nums=[2,3,3]
target=6
print(t.twoSum(nums,target))


