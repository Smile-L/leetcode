class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        line = [1]
        triangle = []
        for i in range(numRows):
             triangle.append(line)       
             #line = [a+b for a,b in zip(line[:-1],line[1:])]
             line = [1]+[a+b for a,b in zip(line[:-1],line[1:])]+[1]
        return triangle
s = Solution()
print s.generate(5)
