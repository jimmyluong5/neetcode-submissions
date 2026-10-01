class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}
        for num in nums:
            if num in map:
                #increase the frequency first
                map[num] += 1
                #check if the frequency > n//2
                if map[num] > n//2:
                    return num
            else:
                #add it to the hashmap
                map[num] = 1
        return num