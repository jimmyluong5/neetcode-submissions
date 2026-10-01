class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a hashmap
        map = {}

        #iterate over both values and indices
        for i, n in enumerate(nums):
            #searching for diff = target-num
            diff = target-n
            if diff in map:
                return [map[diff], i]
        
        #if its not in the hashmap then we add it to the hashmap
            map[n] = i
