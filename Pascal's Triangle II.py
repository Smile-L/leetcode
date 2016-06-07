class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        line = [1]
        triangle = []
        for i in range(rowIndex):
             #line = [a+b for a,b in zip(line[:-1],line[1:])]
             line = [1]+[a+b for a,b in zip(line[:-1],line[1:])]+[1]
        return line

s = Solution()
print s.generate(0)
