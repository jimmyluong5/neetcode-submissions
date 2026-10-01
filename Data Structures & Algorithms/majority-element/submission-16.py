class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}

        #edge case
        if n == 1:
            return nums[0]
        for num in nums:
            if num in map:
                if map[num] == n//2: #majority element guaranteed to exist so this must be true.
                    return num
                else:
                    #increase the frequency
                    map[num] +=1
            else:
                map[num] = 1
        return num
                    