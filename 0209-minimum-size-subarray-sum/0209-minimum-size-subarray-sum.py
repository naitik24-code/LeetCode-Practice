class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        windowSum=0
        result=float('inf')
        for right in range(len(nums)):
            windowSum+=nums[right]
            while windowSum>=target:
                result=min(result,right-left+1)
                windowSum-=nums[left]
                left+=1
        if result == float('inf'):
            return 0
        return result
        