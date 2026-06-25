class Solution(object):
    def twoSum(self, nums, target):
        numMap={}
        for i in range (len(nums)):
            complement=target-nums[i]
            if complement in numMap:
                return[numMap[complement],i]
            numMap[nums[i]]=i