class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #has hashmap and check the frequency
        map = {}
        for num in nums:
            if num in map:
                #if the occurence is more than 1 or greater than 1
                if map[num] >=1:
                    return True
            #add it to the hashmap
            map[num] = 1
        return False