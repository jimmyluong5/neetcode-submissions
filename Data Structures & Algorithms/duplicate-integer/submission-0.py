class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #just use a hashmap and count the frequency of the numbers
        map = {}

        for n in nums:
            #if the number is already in the hashmap increase its frequency then return true or just return true.
            if n in map:

                return True
            else:
                #add it to the hashmap
                map[n] = 1
        return False
                
                