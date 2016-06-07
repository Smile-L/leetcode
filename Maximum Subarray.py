class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = -999999
        sums = 0
        for num in nums:
            if num<=0 and num>sub:
                sub = num
            sums = sums+num
            if sums<0:
                sums = 0

            if sums>0 and sums>sub:
                sub = sums
        return sub