class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #hashmap question if the frequency is greater is equal to n/2 then return that value
        map = {}
        
        n = len(nums)
        
        for num in nums:
            if num in map:
                #increase freq
                map[num] +=1
            else:
                map[num] = 1
            if map[num] > n//2:
                return num
        return num