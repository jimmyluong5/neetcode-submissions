class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1


        while left <= right:
            #constantly calculate the middle ptr
            middle = int(left + (right-left)/2)
            if target > nums[middle]:
                #the target is greater than the middle number
                #so it must be towards the right side of the array
                #move the left ptr to middle+1
                left = middle + 1
            elif target < nums[middle]:
                #target is on the left side, so move the right ptr to middle-1
                right = middle-1
            else: 
                return middle
        return -1
        

            

                