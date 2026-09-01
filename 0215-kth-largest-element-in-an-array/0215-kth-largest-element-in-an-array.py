class Solution(object):
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        def quickselect(left, right):
            pivot = nums[(left+right)//2]
            low=left
            i=left
            high=right
            while i<=high:
                if nums[i]<pivot:
                    nums[low],nums[i]=nums[i],nums[low]
                    low+=1
                    i+=1
                elif nums[i]>pivot:
                    nums[i],nums[high]=nums[high],nums[i]
                    high-=1
                else:
                    i+=1
            if target<low:
                return quickselect(left,low-1)
            elif target>high:
                return quickselect(high+1,right)
            else:
                return nums[target]
        return quickselect(0,len(nums)-1)
