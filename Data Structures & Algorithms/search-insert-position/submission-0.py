class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #set up binary search
        left = 0
        right = len(nums)-1

        while left <=right:
            mid = left +(right-left)//2
            
            if target > nums[mid]:
                left = mid+1
            
            elif target< nums[mid]:
                right = mid-1
            
            else:
                return mid
        #return left or right, when they are on top of each other it would be that index then +1
        return left