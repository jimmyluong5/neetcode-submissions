class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if we are searching, then we must use binary search
        #we are looking for the index of target
        #use two pointers since its binary search
        #isnt this just looking for target?

        #makes it more complicated because of the array is rotated, the left and right pointers don't
        #work because its not sorted technically

        #i could sort it using mergesort but thats O(nlogn)

        #theres a pivot point and at that point both halves are sorted respectively, if you 
        #compare target with the values like that binary search can work

        #like because both halves will be sorted, well focus on 1 half first, if you know one half is sorted
        #you can perform binary search between nums[left] and nums[mid], if its in between this range
        #move right to mid-1 and vice versa

        #but we need to figure out how to determine which half is sorted.

        #to figure out if the left half is sorted,
        #if nums[left] < nums[mid]: then its sorted in ascending order, because the number in the middle
        #must always be larger than the number on the left. 
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+abs((right-left))//2

            if target==nums[mid]:
                return mid

            if nums[left] <= nums[mid]: # <= because if target is less than nums[left] we know its in the right half.
                #so we looking at the left half
                #we need to check if target is in between nums[left] and nums[mid]
                if nums[left]<= target <= nums[mid]:
                    #then we move the right pointer so we look in the left half.
                    right = mid-1
                else:
                    #we move the left pointer if target is not in the left array
                    left = mid+1
            else: #look at right array
                #we in the right half
                #check if target is between nums[mid] and nums[right]
                if nums[mid] <= target <= nums[right]:
                    #we move the left pointer to search the right array
                    left = mid+1
                else:
                    #search in left array
                    right = mid-1
            
        return -1

                