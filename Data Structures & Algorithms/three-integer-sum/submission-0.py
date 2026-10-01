class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #so add nums[i]+nums[j]+nums[k] ==0 thats the condition.
        #we need to sort the array 

        #store the result
        res = []
        #sort the array
        nums.sort()
        #then we need to place a pointer at the left end of the sorted array
        #then we will have a left and right pointer to find 

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: #if our value is equal to the previous value then we continue and select it as the first number (a)
                continue
            #then we need to create the left and right pointers
            left = i+1
            right = len(nums)-1
            while left<right:
                #calculate the sum
                sum = num+nums[left]+nums[right]
                #then if the sum is too small like negative we need to move the left pointer up
                if sum < 0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    #we need to add the values at the left, right and num to our res
                    res.append([num, nums[left], nums[right]])
                    #we need to move our left pointer in case we find a duplicate neg num
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        #move the left pointer
                        left+=1

        return res

