class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use hashmap 
        map = {}
        for num in nums:
            if num in map:
                return True
            else:
                #add to map
                map[num]=1
        return False