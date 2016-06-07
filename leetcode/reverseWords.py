class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = []
        t = []
        for ss in s:
            if ss == ' 'and t!=[]:
                t = ''.join(t)
                t = str(t)
                rs.append(t)
                t = []
            elif ss!=' ':t.append(ss)
        if t!=[]:
            t = ''.join(t)
            t = str(t)
            rs.append(t)
        if len(rs)==0:return ''
        rs.reverse()
        return ' '.join(rs)
    def reverseWordssmart(self,s):
        return ' '.join(s.split()[::-1])
w = 'hello the new world'
s = Solution()
rw = s.reverseWords(w)
print rw
