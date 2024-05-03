class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #Comment the Approach which you dont require

        #Approach 0
        if target in nums:
            return nums.index(target)
        else:
            return -1

        #Approach 1

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

        #Approach 2
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            i+=1
        return -1
