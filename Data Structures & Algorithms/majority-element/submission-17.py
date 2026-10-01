class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}

        #edge case
        if n == 1:
            return nums[0]
        for num in nums:
            if num in map:
                map[num] +=1
                if map[num] > n//2:
                    return num
            else:
                map[num] = 1
        return num
                    