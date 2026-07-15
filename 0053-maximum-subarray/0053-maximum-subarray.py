class Solution(object):
    def maxSubArray(self, nums):
        currentSum=0
        maxSum=nums[0]
        for num in nums:
            if currentSum<0:
                currentSum=0
            currentSum += num
            maxSum=max(maxSum,currentSum)
        return maxSum
        