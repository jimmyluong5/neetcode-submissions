class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #left and right initialized to the 2nd position in the array
        left = 1
        #each time we see a unique value then we must place it where the left index is
        #the first value in the array we don't care so we start at 1st index.

        #iterate through the array
        for right in range(1, len(nums)): #start right at the first index.
            #if right pointer and the right-1 pointer is not equal, then we can swap the values
            #because we have a unique number thats not a duplicate.
            if nums[right] != nums[right-1]:
                #replace the left value with the unique value
                nums[left] = nums[right]
                #then move the left pointer for a spot for a unique spot.
                left+=1
            #else, the right pointer keeps scanning until we see a unique value
        return left


