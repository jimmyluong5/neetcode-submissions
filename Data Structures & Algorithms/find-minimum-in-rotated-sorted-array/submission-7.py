class Solution:
    def findMin(self, nums: List[int]) -> int:
        #two pointer approach and binary search
        left = 0
        right = len(nums)-1
        min_val = 0
        while left <= right:
            #calculate mid
            mid = left + (right-left)//2
            if left == right:
                return nums[left]

            if nums[left] < nums[right]:
                #right = mid-1
                #min_val = nums[left]
                return nums[left]
            
            else: # nums[right] < nums[left] #then check if 
                if nums[mid] < nums[right]: #which it will be
                    min_val = nums[mid]
                #either the minimum will be on the left of mid, so we move the right pointer to mid-1
                    #then move the right pointer to mid
                    right = mid
                else:
                    #nums[mid] >= nums[right] 
                    #then the smallest value is just mid or the right of mid

                    #so move left to mid+1 because the smaller number will be on the right of mid. and check the right side
                    left = mid+1


        return min_val
            #we need to compare min_vals 

        