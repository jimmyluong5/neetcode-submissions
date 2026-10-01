class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #two ptr 
        i = 0
        j = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                
                #move the j ptr
                k +=1
                j +=1
        
        return k

        