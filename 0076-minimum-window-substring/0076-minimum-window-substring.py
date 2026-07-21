class Solution(object):
    def minWindow(self, s, t):
        if len(t)>len(s):
            return ""
        need=Counter(t)
        window={}
        have=0
        needCount=len(need)
        result=[-1,-1]
        resultLen=float("inf")
        left=0
        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char,0)+1
            if char in need and window[char]==need[char]:
                have+=1
            while have==needCount:
                if (right-left+1)<resultLen:
                    result=[left,right]
                    resultLen=right-left+1
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        left,right=result
        return s[left:right+1] if resultLen != float("inf") else ""
        