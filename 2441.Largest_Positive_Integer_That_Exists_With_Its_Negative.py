class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxNumber = -1
        for num in nums:
            if -num in nums:
                maxNumber = max(maxNumber,abs(num)) 
        return maxNumber