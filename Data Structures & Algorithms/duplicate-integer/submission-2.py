class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #so if the frequency is greater than 1 then return true else return flase
    #make hashmap
        map = {}
        for num in nums:
            if num in map:
                map[num] +=1
                return True
            else:
                map[num] = 1
        return False