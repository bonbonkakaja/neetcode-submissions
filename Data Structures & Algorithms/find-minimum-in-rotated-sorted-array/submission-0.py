class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while(nums[left]>nums[right]):
            mid=(left+right)//2
            if(nums[left]<nums[mid]):
                left=mid
            elif(nums[right]>nums[mid]):
                right=mid
            elif(left == mid):
                return nums[right]
        
        return nums[left]

            
        
        