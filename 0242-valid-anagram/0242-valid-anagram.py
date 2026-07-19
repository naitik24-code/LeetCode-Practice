class Solution(object):
    def isAnagram(self, s, t):
        s1=sorted(s)
        s2=sorted(t)

        return s1==s2
        