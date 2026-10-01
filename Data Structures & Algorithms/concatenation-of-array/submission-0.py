class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create the ans array with a size of 2n where n is the size of nums

        n = len(nums)
        ans = [0] * (2*n)

        #then we loop from 0 to n
        for i in range(n):
            #we assign ans[i] = nums[i] #which fills the first half of the array
            #then ans[i+n] = nums[i] which fills the 2nd half of the array
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans