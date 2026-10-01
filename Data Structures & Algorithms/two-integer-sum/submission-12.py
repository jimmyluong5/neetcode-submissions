class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #create hashmap
        map = {}
        
        #iterate over the values and the indices
        for i, n in enumerate(nums):
            #calculate diff each iteration
            diff = target-n
            if diff in map: #if the number is in the hashmap already then return the indices
                return [map[diff],i]
            else:
                #we add it to the hashmap
                map[n] = i