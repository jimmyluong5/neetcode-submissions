class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #map
        map = {}
        for i, num in enumerate(nums):
            #calculate diff 
            diff = target-num
            if diff in map:
                return [map[diff], i]
            map[num] = i
        