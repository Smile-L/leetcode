class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = []
        for i,num in enumerate(nums):
            if num  in left:
                return [left.index(num),i]
            else:
                left.append(target-num)
            print left
        return None

s = Solution()
nums = [2, 7, 11, 15]
target = 9
print s.twoSum(nums,target)

