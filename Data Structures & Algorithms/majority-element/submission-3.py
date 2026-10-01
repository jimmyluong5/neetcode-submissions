class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #edge case is if the array is empty or size 1
        n = len(nums)
        if n == 1:
            return nums[0] #return the first element
        
        #create hashmap
        map = {}

        for num in nums:
            if num in map:
                #check its frequency if its equal to n/2 then return that key value
                if map[num] == n//2:
                    return num
            
                else:
                    #increase the frequency
                    map[num] +=1
            else:
                #add it to the hashmap
                map[num] = 1
        return num