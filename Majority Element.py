class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        maxnum = nums[0]
        maxtime = 0
        for num in nums :
            if num in num_dict:
                num_dict[num] =  num_dict[num]  +1
            else:
                num_dict[num] = 1
            if num_dict[num]>maxtime :
                maxtime = num_dict[num]
                maxnum = num
        return maxnum